from abc import ABC, abstractmethod

from fastapi_proj.domain.enteties.user import User


class BaseUserRepository(ABC):
    @abstractmethod
    async def get_or_create_new(self, username: str) -> User: ...

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

    @abstractmethod
    async def check_is_recipe_liked(self, username: str, recipe_id: str) -> bool: ...
