from pprint import pprint
from typing import Annotated

from fastapi import APIRouter, Depends
from punq import Container

from fastapi_proj.application.recipes.schemas import (
    ComponentResponceSchema,
    CreateComponentShema,
    ListOfComponentsResponceSchema,
)
from fastapi_proj.domain.enteties.component import (
    ComponentCategory,
    Ingredient,
)
from fastapi_proj.domain.values.components import CommonTitle, IngredientAmount
from fastapi_proj.infra.container import init_container
from fastapi_proj.logic.comands.ingredients import (
    CreateComponentCommand,
    GetComponentByTitleCommand,
    GetComponentsByCategory,
)
from fastapi_proj.logic.mediator import Mediator

router = APIRouter(prefix="/components", tags=["components"])


@router.post("")
async def create_ingredient(
    component: CreateComponentShema,
    container: Annotated[Container, Depends(init_container)],
):
    mediator: Mediator = container.resolve(Mediator)  # type: ignore
    ingredients = [
        Ingredient(
            CommonTitle(ingredient.title), IngredientAmount(ingredient.amount)
        )
        for ingredient in component.ingredients
    ]
    command = CreateComponentCommand(
        CommonTitle(component.title),
        ComponentCategory(component.component_category),
        ingredients,
    )
    await mediator.handle_command(command)


@router.get("/", response_model=ListOfComponentsResponceSchema)
async def get_components_by_category(
    category: ComponentCategory,
    container: Annotated[Container, Depends(init_container)],
    limit: int = 10,
    offset: int = 0,
):
    mediator: Mediator = container.resolve(Mediator)  # type: ignore
    command = GetComponentsByCategory(category, limit, offset)
    result, *_ = await mediator.handle_command(command)
    return {"components": result}


@router.get("{component_title}", response_model=ComponentResponceSchema)
async def get_one_ingredient_by_id(
    component_title: str,
    container: Annotated[Container, Depends(init_container)],
):
    mediator: Mediator = container.resolve(Mediator)  # type: ignore
    command = GetComponentByTitleCommand(CommonTitle(component_title))
    result, *_ = await mediator.handle_command(command)
    return result


@router.put("{ingredient_name}")
async def change_ingredient(ingredient_name: str): ...
