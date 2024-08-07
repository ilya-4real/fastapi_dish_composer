from logging import getLogger
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse

from fastapi_proj.application.dependencies import (
    get_mediator,
    get_query_mediator,
    get_user,
)
from fastapi_proj.application.recipies.schemas import (
    RecipesResponceSchema,
    SearchRecipesSchema,
)
from fastapi_proj.application.schemas import (
    CreateRecipeSchema,
    ExceptionSchema,
    RecipeResponceSchema,
    UpdateRecipeSchema,
)
from fastapi_proj.domain.enteties.component import (
    Component,
    ComponentCategory,
    Ingredient,
)
from fastapi_proj.domain.enteties.user import User
from fastapi_proj.domain.values.components import CommonTitle, IngredientAmount
from fastapi_proj.logic.comands.recipe import (
    CreateRecipeCommand,
    GenerateRandomRecipeCommand,
    LikeRecipeCommand,
    UpdateRecipeCommand,
)
from fastapi_proj.logic.mediator import Mediator
from fastapi_proj.logic.queries.recipes import (
    GetPopularRecipesQuery,
    GetRecipeByIdQuery,
    SearchQuery,
)
from fastapi_proj.logic.querymediator import QueryMediator

logger = getLogger(__name__)

router = APIRouter(prefix="/recipies", tags=["recipies"])


@router.post("/")
async def create_recipe(
    recipe: CreateRecipeSchema, mediator: Annotated[Mediator, Depends(get_mediator)]
):
    components: list[Component] = []
    for component in recipe.components:
        ingredients: list[Ingredient] = []
        for ingredient in component.ingredients:
            ingr = Ingredient(
                CommonTitle(ingredient.title), IngredientAmount(ingredient.amount)
            )
            ingredients.append(ingr)
        components.append(
            Component(
                CommonTitle(component.title), ComponentCategory("none"), ingredients
            )
        )
    command = CreateRecipeCommand(
        recipe.title, recipe.author, recipe.description or "", components
    )
    await mediator.handle_command(command)


@router.get("/popular", response_model=RecipesResponceSchema)
async def get_popular_recipes(
    mediator: Annotated[QueryMediator, Depends(get_query_mediator)],
    limit: int = 10,
    offset: int = 0,
):
    command = GetPopularRecipesQuery(limit, offset)
    result = await mediator.handle_query(command)
    return RecipesResponceSchema.model_validate({"recipes": result})


@router.get(
    "/search", responses={200: {"model": SearchRecipesSchema}, 204: {"model": None}}
)
async def search_for_recipe(
    q: str, mediator: Annotated[QueryMediator, Depends(get_query_mediator)]
):
    result = await mediator.handle_query(SearchQuery(q))
    if not result:
        return Response(None, status_code=204)
    return SearchRecipesSchema.model_validate({"recipes": result})


@router.get("/random", response_model=RecipeResponceSchema)
async def generate_random_recipe(
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    command = GenerateRandomRecipeCommand()
    result, *_ = await mediator.handle_command(command)
    return RecipeResponceSchema.model_validate(result)


@router.get(
    "/{recipe_id}",
    responses={200: {"model": RecipeResponceSchema}, 404: {"model": None}},
)
async def get_recipe_detail(
    user: Annotated[User, Depends(get_user)],
    recipe_id: str,
    mediator: Annotated[QueryMediator, Depends(get_query_mediator)],
):
    command = GetRecipeByIdQuery(user.username, recipe_id)
    result = await mediator.handle_query(command)
    if not result:
        return Response(None, 404)
    return RecipeResponceSchema.model_validate(result)


@router.put(
    "/{recipe_id}",
    responses={
        200: {"model": None},
        401: {"model": ExceptionSchema},
        403: {"model": ExceptionSchema},
    },
)
async def update_recipe(
    recipe_id: str,
    author: Annotated[User, Depends(get_user)],
    new_recipe: UpdateRecipeSchema,
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    command = UpdateRecipeCommand(
        author.username,
        recipe_id,
        new_recipe.title,
        new_recipe.description,
        new_recipe.model_dump()["components"],
    )

    result, *_ = await mediator.handle_command(command)
    return JSONResponse(None, 200)


@router.post("/{recipe_id}/like")
async def like_recipe(
    recipe_id: str,
    user: Annotated[User, Depends(get_user)],
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    command = LikeRecipeCommand(recipe_id, user.username)
    await mediator.handle_command(command)
