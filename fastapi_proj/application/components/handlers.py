import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Response

from fastapi_proj.application.components.schemas import (
    ComponentResponceSchema,
    CreateComponentShema,
    ListOfComponentsResponceSchema,
    UpdateComponentSchema,
)
from fastapi_proj.application.dependencies import get_mediator, get_query_mediator
from fastapi_proj.domain.enteties.component import (
    ComponentCategory,
    Ingredient,
)
from fastapi_proj.domain.values.components import CommonTitle, IngredientAmount
from fastapi_proj.logic.comands.components import (
    CreateComponentCommand,
    DeleteComponentByTitleCommand,
    GetComponentsByCategory,
    UpdateComponentByTitleCommand,
)
from fastapi_proj.logic.mediator import Mediator
from fastapi_proj.logic.queries.components import (
    GetRandomComponentInCategoryQuery,
    QueryComponentById,
)
from fastapi_proj.logic.querymediator import QueryMediator

router = APIRouter(prefix="/components", tags=["components"])

logger = logging.getLogger(__name__)


@router.post("", responses={201: {"model": None}})
async def create_component(
    component: CreateComponentShema,
    mediator: Annotated[Mediator, Depends(get_mediator)],
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
    mediator: Annotated[Mediator, Depends(get_mediator)],
    limit: int = 10,
    offset: int = 0,
):
    command = GetComponentsByCategory(category, limit, offset)
    result, *_ = await mediator.handle_command(command)
    return {"components": result}


@router.get("/random", response_model=ComponentResponceSchema)
async def get_one_random_component_in_category(
    category: ComponentCategory,
    query_mediator: Annotated[QueryMediator, Depends(get_query_mediator)],
):
    query = GetRandomComponentInCategoryQuery(category)
    result = await query_mediator.handle_query(query)
    return result


@router.get(
    "/{component_id}",
    responses={404: {"model": None}, 200: {"model": ComponentResponceSchema}},
)
async def get_one_component_by_title(
    component_id: str,
    mediator: Annotated[QueryMediator, Depends(get_query_mediator)],
):
    query = QueryComponentById(component_id)
    result = await mediator.handle_query(query)
    logger.debug(result)
    if not result:
        return Response(status_code=404)
    return ComponentResponceSchema.model_validate(result)


@router.delete("/{component_id}", responses={204: {"model": None}})
async def delete_component_by_title(
    component_id: str,
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    command = DeleteComponentByTitleCommand(component_id)
    result, *_ = await mediator.handle_command(command)
    return Response(status_code=204)


@router.put("/{component_id}")
async def update_ingredients(
    component_id: str,
    category: ComponentCategory,
    component: UpdateComponentSchema,
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    ingredients = [
        Ingredient(CommonTitle(ingredient.title), IngredientAmount(ingredient.amount))
        for ingredient in component.ingredients
    ]
    command = UpdateComponentByTitleCommand(
        CommonTitle(component_id), category, ingredients
    )

    result, *_ = await mediator.handle_command(command)
