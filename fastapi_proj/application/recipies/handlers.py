from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi_proj.application.dependencies import get_mediator
from fastapi_proj.application.recipies.schemas import CreateRecipeSchema
from fastapi_proj.domain.enteties.component import (
    Component,
    ComponentCategory,
    Ingredient,
)
from fastapi_proj.domain.values.components import CommonTitle, IngredientAmount
from fastapi_proj.logic.comands.recipe import CreateRecipeCommand
from fastapi_proj.logic.mediator import Mediator

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


@router.get("/{recipe_id}")
async def get_recipe_detail(recipe_id: str): ...


@router.delete("/{recipe_id}")
async def delete_recipe(recipe_id: str): ...


@router.put("/{recipe_id}")
async def update_recipe(recipe_id: str): ...


@router.post("/{recipe_id}/like")
async def like_recipe(): ...


@router.post("/{recipe_id}/unlike")
async def unlike_recipe(): ...


@router.get("/random")
async def generate_random_recipe(): ...


@router.get("/popular")
async def get_popular_recipes(limit: int = 10, offset: int = 0): ...
