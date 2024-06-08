from abc import ABC, abstractmethod


class BaseUserRepository(ABC):
    @abstractmethod
    async def create_new(self, username: str) -> None: ...

    @abstractmethod
    async def add_created_recipe(self, username: str, recipe_id: str) -> None: ...

    @abstractmethod
    async def add_liked_recipe(self, username: str, recipe_id: str) -> None: ...
