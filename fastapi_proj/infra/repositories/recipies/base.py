from abc import ABC, abstractmethod
from dataclasses import dataclass

from fastapi_proj.domain.enteties.component import Component, ComponentCategory
from fastapi_proj.domain.enteties.recipe import Recipe


@dataclass(eq=False)
class BaseRecipeRepository(ABC):
    @abstractmethod
    async def add_recipe(self, recipe: Recipe) -> None: ...


@dataclass
class BaseComponentRepository(ABC):
    @abstractmethod
    async def add_component(self, ingredient: Component) -> None: ...

    @abstractmethod
    async def get_random_component_by_category(
        self, category: ComponentCategory
    ) -> Component: ...
