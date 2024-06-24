from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from fastapi_proj.domain.enteties.component import Component, ComponentCategory
from fastapi_proj.domain.enteties.recipe import Recipe


@dataclass(eq=False)
class BaseRecipeRepository(ABC):
    @abstractmethod
    async def add_recipe(self, recipe: Recipe) -> None: ...

    @abstractmethod
    async def get_by_id(self, recipe_id: str) -> dict | None: ...

    @abstractmethod
    async def increase_likes(self, recipe_id: str) -> None: ...

    @abstractmethod
    async def decrease_likes(self, recipe_id: str) -> None: ...

    @abstractmethod
    async def get_popular_recipes(self, limit: int, offset: int) -> list: ...

    @abstractmethod
    async def search_for_recipe(self, q: str) -> list[dict] | None: ...


@dataclass
class BaseComponentRepository(ABC):
    @abstractmethod
    async def add_component(self, ingredient: Component) -> None: ...

    @abstractmethod
    async def get_random_component_by_category(
        self, category: ComponentCategory
    ) -> dict[str, Any]: ...

    @abstractmethod
    async def get_components_by_category(
        self, category: str, limit: int, offset: int
    ) -> list[dict]: ...

    @abstractmethod
    async def get_component_by_id(self, title: str) -> dict: ...

    @abstractmethod
    async def delete_by_id(self, recipe_id: str) -> None: ...

    @abstractmethod
    async def update_one_component_ingredients(self, component: Component) -> None: ...
