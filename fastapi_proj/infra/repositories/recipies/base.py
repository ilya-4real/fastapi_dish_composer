from abc import ABC, abstractmethod
from dataclasses import dataclass

from fastapi_proj.domain.enteties.recipe import Recipe


@dataclass(eq=False)
class BaseRecipeRepository(ABC):
    @abstractmethod
    async def add_recipe(self, recipe: Recipe): ...
