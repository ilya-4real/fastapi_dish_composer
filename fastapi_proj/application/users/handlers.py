from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi_proj.application.dependencies import get_mediator
from fastapi_proj.application.users.schemas import UserCreateSchema
from fastapi_proj.logic.comands.users import CreateUserCommand
from fastapi_proj.logic.mediator import Mediator

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def create_user(
    user: UserCreateSchema, mediator: Annotated[Mediator, Depends(get_mediator)]
):
    command = CreateUserCommand(user.username)
    await mediator.handle_command(command)


@router.get("/{username}/recipes")
async def get_users_recipes(username: str): ...


@router.get("/{username}/liked")
async def get_users_liked_recipes(username: str): ...
