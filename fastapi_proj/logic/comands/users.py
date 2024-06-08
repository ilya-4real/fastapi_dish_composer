from dataclasses import dataclass

from fastapi_proj.infra.repositories.users.base import BaseUserRepository
from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    username: str


@dataclass
class CreateUserHandler(BaseCommandHandler[CreateUserCommand, None]):
    user_repository: BaseUserRepository

    async def handle(self, command: CreateUserCommand) -> None:
        await self.user_repository.create_new(command.username)
