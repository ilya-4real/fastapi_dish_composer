from abc import ABC, abstractmethod


class BaseUserRepository(ABC):
    @abstractmethod
    async def create_new(self, username: str) -> None: ...

    @abstractmethod
    async def add_created_recipe(self, username: str, recipe_id: str) -> None: ...

    @abstractmethod
    async def add_liked_recipe(self, username: str, recipe_id: str) -> None: ...

    @abstractmethod
    async def remove_liked_recipe(self, username: str, recipe_id: str) -> None: ...

    @abstractmethod
    async def get_liked_recipes_by_username(self, username: str) -> dict: ...

    @abstractmethod
    async def get_created_recipes_by_username(self, username: str) -> dict: ...
