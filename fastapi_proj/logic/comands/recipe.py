from dataclasses import dataclass

from fastapi_proj.domain.enteties.recipe import Recipe
from fastapi_proj.infra.repositories.recipies.base import BaseComponentRepository
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
