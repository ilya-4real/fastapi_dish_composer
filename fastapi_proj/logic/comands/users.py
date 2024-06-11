from dataclasses import dataclass

from fastapi_proj.domain.enteties.user import User
from fastapi_proj.infra.repositories.users.base import BaseUserRepository
from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class GetOrCreateUserCommand(BaseCommand):
    username: str


@dataclass
class GetOrCreateUserHandler(BaseCommandHandler[GetOrCreateUserCommand, None]):
    user_repository: BaseUserRepository

    async def handle(self, command: GetOrCreateUserCommand) -> User:
        user = await self.user_repository.get_or_create_new(command.username)
        return user


@dataclass(frozen=True)
class GetUserCreatedRecipesCommand(BaseCommand):
    username: str


@dataclass
class GetUserCreatedRecipesHandler(
    BaseCommandHandler[GetUserCreatedRecipesCommand, dict]
):
    user_repository: BaseUserRepository

    async def handle(self, command: GetUserCreatedRecipesCommand) -> dict:
        return await self.user_repository.get_created_recipes_by_username(
            command.username
        )


@dataclass(frozen=True)
class GetUserLikedRecipesCommand(BaseCommand):
    username: str


@dataclass
class GetUserLikedRecipesHandler(BaseCommandHandler[GetUserLikedRecipesCommand, list]):
    user_repository: BaseUserRepository

    async def handle(self, command: GetUserLikedRecipesCommand) -> dict:
        return await self.user_repository.get_liked_recipes_by_username(
            command.username
        )
