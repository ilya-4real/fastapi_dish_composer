from dataclasses import dataclass

from fastapi_proj.domain.enteties.recipe import Recipe
from fastapi_proj.infra.repositories.recipies.base import BaseRecipeRepository


@dataclass
class MongoRecipeRepository(BaseRecipeRepository):
    async def add_recipe(self, recipe: Recipe): ...
