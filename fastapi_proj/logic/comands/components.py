from dataclasses import dataclass
from logging import getLogger

from fastapi_proj.domain.enteties.component import (
    Component,
    ComponentCategory,
    Ingredient,
)
from fastapi_proj.domain.values.components import CommonTitle
from fastapi_proj.infra.repositories.recipies.base import (
    BaseComponentRepository,
)
from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler

logger = getLogger(__name__)


@dataclass(frozen=True)
class CreateComponentCommand(BaseCommand):
    title: CommonTitle
    category: ComponentCategory
    ingredients: list[Ingredient]


@dataclass(frozen=True)
class GetComponentsByCategory(BaseCommand):
    category: ComponentCategory
    limit: int
    offset: int


@dataclass(frozen=True)
class DeleteComponentByTitleCommand(BaseCommand):
    oid: str


@dataclass(frozen=True)
class UpdateComponentByTitleCommand(BaseCommand):
    title: CommonTitle
    category: ComponentCategory
    ingredients: list[Ingredient]


@dataclass
class CreateComponentCommandHandler(BaseCommandHandler[CreateComponentCommand, str]):
    component_repository: BaseComponentRepository

    async def handle(self, command):
        component = Component(command.title, command.category, command.ingredients)
        await self.component_repository.add_component(component)


@dataclass
class GetComponentsByCategoryHandler(
    BaseCommandHandler[GetComponentsByCategory, list[Component]]
):
    component_repository: BaseComponentRepository

    async def handle(self, command: GetComponentsByCategory) -> list[dict]:
        result = await self.component_repository.get_components_by_category(
            command.category.name, command.limit, command.offset
        )

        return result


@dataclass
class DeleteComponentByTitleHandler(
    BaseCommandHandler[DeleteComponentByTitleCommand, None]
):
    component_repository: BaseComponentRepository

    async def handle(self, command: DeleteComponentByTitleCommand) -> None:
        return await self.component_repository.delete_by_id(command.oid)


@dataclass
class UpdateComponentByTitleHandler(
    BaseCommandHandler[UpdateComponentByTitleCommand, None]
):
    component_repository: BaseComponentRepository

    async def handle(self, command: UpdateComponentByTitleCommand) -> None:
        component = Component(command.title, command.category, command.ingredients)
        result = await self.component_repository.update_one_component_ingredients(
            component
        )
        return result
