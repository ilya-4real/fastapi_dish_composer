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
