from dataclasses import dataclass
from logging import getLogger

from fastapi_proj.domain.enteties.component import Component, ComponentCategory
from fastapi_proj.domain.enteties.recipe import Recipe
from fastapi_proj.infra.repositories.recipies.base import (
    BaseComponentRepository,
    BaseRecipeRepository,
)
from fastapi_proj.infra.repositories.users.base import BaseUserRepository
from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler

logger = getLogger(__name__)


@dataclass(frozen=True)
class GenerateRandomRecipeCommand(BaseCommand): ...


@dataclass
class GenerateRandomRecipeHandler(
    BaseCommandHandler[GenerateRandomRecipeCommand, Recipe]
):
    component_repository: BaseComponentRepository

    async def handle(self, command: GenerateRandomRecipeCommand) -> dict:
        meat = await self.component_repository.get_random_component_by_category(
            ComponentCategory("meat")
        )
        garnish = await self.component_repository.get_random_component_by_category(
            ComponentCategory("garnish")
        )
        sauce = await self.component_repository.get_random_component_by_category(
            ComponentCategory("sauce")
        )

        recipe = {
            "title": f"{meat['title']}, {garnish['title']}, {sauce['title']}",
            "description": "",
            "components": [meat, garnish, sauce],
            "likes": 0,
            "author": "Builder",
        }

        # logger.debug(recipe)

        return recipe


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


@dataclass(frozen=True)
class LikeRecipeCommand(BaseCommand):
    recipe_id: str
    author_id: str


@dataclass
class LikeRecipeHandler(BaseCommandHandler[LikeRecipeCommand, None]):
    recipe_repository: BaseRecipeRepository
    user_repository: BaseUserRepository

    async def handle(self, command: LikeRecipeCommand) -> None:
        is_liked = await self.user_repository.check_is_recipe_liked(
            command.author_id, command.recipe_id
        )
        if is_liked:
            await self.user_repository.remove_liked_recipe(
                command.author_id, command.recipe_id
            )
            await self.recipe_repository.decrease_likes(command.recipe_id)
        else:
            await self.recipe_repository.increase_likes(command.recipe_id)
            await self.user_repository.add_liked_recipe(
                command.author_id, command.recipe_id
            )
