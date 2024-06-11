from typing import Annotated

from fastapi import Depends
from punq import Container

from fastapi_proj.application.authscheme import auth_scheme
from fastapi_proj.domain.enteties.user import User
from fastapi_proj.infra.container import init_container
from fastapi_proj.logic.comands.users import GetOrCreateUserCommand
from fastapi_proj.logic.mediator import Mediator


def get_mediator(container: Annotated[Container, Depends(init_container)]) -> Mediator:
    mediator: Mediator = container.resolve(Mediator)  # type: ignore
    return mediator


async def get_user(
    username: Annotated[str, Depends(auth_scheme)],
    mediator: Annotated[Mediator, Depends(get_mediator)],
) -> User:
    command = GetOrCreateUserCommand(username)
    user, *_ = await mediator.handle_command(command)
    return user
