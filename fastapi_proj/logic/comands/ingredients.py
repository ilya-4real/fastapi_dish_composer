from dataclasses import dataclass

from fastapi_proj.domain.enteties.component import Component, ComponentCategory
from fastapi_proj.domain.values.ingredient import CommonTitle, IngredientAmount
from fastapi_proj.infra.repositories.recipies.base import (
    BaseComponentRepository,
)
from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class CreateComponentCommand(BaseCommand):
    title: CommonTitle
    category: ComponentCategory
    amount: IngredientAmount


@dataclass
class CreateComponentCommandHandler(
    BaseCommandHandler[CreateComponentCommand, str]
):
    component_repository: BaseComponentRepository

    async def handle(self, command):
        component = Component(command.title, command.category)
        await self.component_repository.add_component(component)
