from dataclasses import dataclass

from fastapi_proj.infra.repositories.users.base import BaseUserRepository
from fastapi_proj.logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class GetUserLikedRecipesQuery(BaseQuery):
    username: str


@dataclass
class GetUserLikedRecipesHandler(BaseQueryHandler[GetUserLikedRecipesQuery, list]):
    user_repository: BaseUserRepository

    async def handle(self, command: GetUserLikedRecipesQuery) -> dict:
        return await self.user_repository.get_liked_recipes_by_username(
            command.username
        )


@dataclass(frozen=True)
class GetUserCreatedRecipesQuery(BaseQuery):
    username: str


@dataclass
class GetUserCreatedRecipesHandler(BaseQueryHandler[GetUserCreatedRecipesQuery, dict]):
    user_repository: BaseUserRepository

    async def handle(self, command: GetUserCreatedRecipesQuery) -> dict:
        return await self.user_repository.get_created_recipes_by_username(
            command.username
        )
