from dataclasses import dataclass

from fastapi_proj.domain.enteties.component import Component
from fastapi_proj.domain.enteties.recipe import Recipe
from fastapi_proj.infra.repositories.recipies.base import (
    BaseComponentRepository,
    BaseRecipeRepository,
)
from fastapi_proj.infra.repositories.users.base import BaseUserRepository
from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class GenerateRandomRecipeCommand(BaseCommand): ...


@dataclass
class GenerateRandomRecipeHandler(
    BaseCommandHandler[GenerateRandomRecipeCommand, Recipe]
):
    component_repository: BaseComponentRepository

    async def handle(self, command: GenerateRandomRecipeCommand) -> Recipe:  # type: ignore
        ...


@dataclass(frozen=True)
class CreateRecipeCommand(BaseCommand):
    title: str
    author: str
    description: str | None
    components: list[Component]


@dataclass
class CreateRecipeHandler(BaseCommandHandler[CreateRecipeCommand, None]):
    recipe_repository: BaseRecipeRepository
    user_repository: BaseUserRepository

    async def handle(self, command: CreateRecipeCommand) -> None:
        recipe = Recipe(
            command.author, command.title, command.description, command.components
        )
        await self.recipe_repository.add_recipe(recipe)
        await self.user_repository.add_created_recipe(command.author, recipe.oid)
