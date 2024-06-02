from dataclasses import dataclass
from typing import Any

from fastapi_proj.domain.enteties.component import (
    Component,
    ComponentCategory,
    Ingredient,
)
from fastapi_proj.domain.values.components import CommonTitle, IngredientAmount
from fastapi_proj.infra.repositories.recipies.base import (
    BaseComponentRepository,
)
from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler


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
class GetComponentByTitleCommand(BaseCommand):
    title: CommonTitle


@dataclass(frozen=True)
class GetRandomComponentInCategoryCommand(BaseCommand):
    category: ComponentCategory


@dataclass
class CreateComponentCommandHandler(
    BaseCommandHandler[CreateComponentCommand, str]
):
    component_repository: BaseComponentRepository

    async def handle(self, command):
        component = Component(
            command.title, command.category, command.ingredients
        )
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
        print(result)
        return result


@dataclass
class GetComponentByTitleHandler(
    BaseCommandHandler[GetComponentByTitleCommand, dict]
):
    component_repository: BaseComponentRepository

    async def handle(self, command: GetComponentByTitleCommand) -> dict:
        return await self.component_repository.get_component_by_title(
            command.title
        )


@dataclass
class GetRandomComponentInCategoryHandler(
    BaseCommandHandler[GetRandomComponentInCategoryCommand, dict[str, Any]]
):
    component_repository: BaseComponentRepository

    async def handle(
        self, command: GetRandomComponentInCategoryCommand
    ) -> dict[str, Any]:
        return (
            await self.component_repository.get_random_component_by_category(
                command.category
            )
        )
