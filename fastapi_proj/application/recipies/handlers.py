from logging import getLogger
from pprint import pprint
from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi_proj.application.dependencies import get_mediator
from fastapi_proj.application.recipies.schemas import (
    QueryRecipesSchema,
    RecipeLikeSchema,
)
from fastapi_proj.application.schemas import CreateRecipeSchema, RecipeResponceSchema
from fastapi_proj.domain.enteties.component import (
    Component,
    ComponentCategory,
    Ingredient,
)
from fastapi_proj.domain.values.components import CommonTitle, IngredientAmount
from fastapi_proj.logic.comands.recipe import (
    CreateRecipeCommand,
    GenerateRandomRecipeCommand,
    GetPopularRecipesCommand,
    GetRecipeByIdCommand,
    LikeRecipeCommand,
    UnlikeRecipeCommand,
)
from fastapi_proj.logic.mediator import Mediator

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
    print(recipe)


@router.get("/popular")
async def get_popular_recipes(
    mediator: Annotated[Mediator, Depends(get_mediator)],
    limit: int = 10,
    offset: int = 0,
):
    command = GetPopularRecipesCommand(limit, offset)
    result, *_ = await mediator.handle_command(command)
    return QueryRecipesSchema.model_validate({"recipes": result})


@router.get("/random")
async def generate_random_recipe(
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    command = GenerateRandomRecipeCommand()
    result, *_ = await mediator.handle_command(command)
    pprint(result)
    return RecipeResponceSchema.model_validate(result)


@router.get("/{recipe_id}")
async def get_recipe_detail(
    recipe_id: str, mediator: Annotated[Mediator, Depends(get_mediator)]
):
    command = GetRecipeByIdCommand(recipe_id)
    result, *_ = await mediator.handle_command(command)
    pprint(result)
    return RecipeResponceSchema.model_validate(result)


@router.delete("/{recipe_id}")
async def delete_recipe(recipe_id: str): ...


@router.put("/{recipe_id}")
async def update_recipe(recipe_id: str): ...


@router.post("/{recipe_id}/like")
async def like_recipe(
    recipe_id: str,
    author: RecipeLikeSchema,
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    command = LikeRecipeCommand(recipe_id, author.author_id)
    await mediator.handle_command(command)


@router.post("/{recipe_id}/unlike")
async def unlike_recipe(
    recipe_id: str,
    author: RecipeLikeSchema,
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    command = UnlikeRecipeCommand(author.author_id, recipe_id)
    await mediator.handle_command(command)
