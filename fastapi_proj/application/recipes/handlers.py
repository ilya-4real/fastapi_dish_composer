import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
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
    DeleteComponentByTitleCommand,
    GetComponentByTitleCommand,
    GetComponentsByCategory,
    GetRandomComponentInCategoryCommand,
)
from fastapi_proj.logic.mediator import Mediator

router = APIRouter(prefix="/components", tags=["components"])

logger = logging.getLogger(__name__)


def get_meditor(container: Annotated[Container, Depends(init_container)]):
    mediator: Mediator = container.resolve(Mediator)  # type: ignore
    return mediator


@router.post("", responses={201: {"model": None}})
async def create_component(
    component: CreateComponentShema,
    mediator: Annotated[Mediator, Depends(get_meditor)],
):
    ingredients = [
        Ingredient(CommonTitle(ingredient.title), IngredientAmount(ingredient.amount))
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
    mediator: Annotated[Mediator, Depends(get_meditor)],
    limit: int = 10,
    offset: int = 0,
):
    command = GetComponentsByCategory(category, limit, offset)
    result, *_ = await mediator.handle_command(command)
    return {"components": result}


@router.get(
    "/{component_title}",
    responses={404: {"model": None}, 200: {"model": ComponentResponceSchema}},
)
async def get_one_component_by_id(
    component_title: str,
    mediator: Annotated[Mediator, Depends(get_meditor)],
):
    command = GetComponentByTitleCommand(CommonTitle(component_title))
    result, *_ = await mediator.handle_command(command)
    logger.debug(result)
    if not result:
        return Response(status_code=404)
    return ComponentResponceSchema.model_validate(result)


@router.delete("/{component_title}", responses={204: {"model": None}})
async def delete_component_by_title(
    component_title: str,
    mediator: Annotated[Mediator, Depends(get_meditor)],
):
    command = DeleteComponentByTitleCommand(CommonTitle(component_title))
    result, *_ = await mediator.handle_command(command)
    return Response(status_code=204)


@router.get("/random", response_model=ComponentResponceSchema)
async def get_one_random_component_in_category(
    category: ComponentCategory,
    mediator: Annotated[Mediator, Depends(get_meditor)],
):
    command = GetRandomComponentInCategoryCommand(category)
    result, *_ = await mediator.handle_command(command)
    return result


@router.put("{component_title}")
async def change_ingredient(component_title: str): ...
