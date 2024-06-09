from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi_proj.application.dependencies import get_mediator
from fastapi_proj.application.schemas import RecipesResponceSchema
from fastapi_proj.application.users.schemas import UserCreateSchema
from fastapi_proj.logic.comands.users import (
    CreateUserCommand,
    GetUserCreatedRecipesCommand,
    GetUserLikedRecipesCommand,
)
from fastapi_proj.logic.mediator import Mediator

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def create_user(
    user: UserCreateSchema, mediator: Annotated[Mediator, Depends(get_mediator)]
):
    command = CreateUserCommand(user.username)
    await mediator.handle_command(command)


@router.get("/{username}/recipes")
async def get_users_recipes(
    username: str, mediator: Annotated[Mediator, Depends(get_mediator)]
):
    command = GetUserCreatedRecipesCommand(username)
    result, *_ = await mediator.handle_command(command)
    return RecipesResponceSchema.model_validate(result)


@router.get("/{username}/liked")
async def get_users_liked_recipes(
    username: str, mediator: Annotated[Mediator, Depends(get_mediator)]
):
    command = GetUserLikedRecipesCommand(username)
    result, *_ = await mediator.handle_command(command)
    return RecipesResponceSchema.model_validate(result)
