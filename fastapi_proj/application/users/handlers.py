from logging import getLogger
from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi_proj.application.dependencies import get_mediator, get_user
from fastapi_proj.application.schemas import RecipesResponceSchema
from fastapi_proj.domain.enteties.user import User
from fastapi_proj.logic.comands.users import (
    GetUserCreatedRecipesCommand,
    GetUserLikedRecipesCommand,
)
from fastapi_proj.logic.mediator import Mediator

logger = getLogger(__name__)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/recipes")
async def get_users_recipes(
    user: Annotated[User, Depends(get_user)],
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    logger.debug(user)
    command = GetUserCreatedRecipesCommand(user.username)
    result, *_ = await mediator.handle_command(command)
    return RecipesResponceSchema.model_validate(result)


@router.get("/liked")
async def get_users_liked_recipes(
    user: Annotated[User, Depends(get_user)],
    mediator: Annotated[Mediator, Depends(get_mediator)],
):
    command = GetUserLikedRecipesCommand(user.username)
    result, *_ = await mediator.handle_command(command)
    return RecipesResponceSchema.model_validate(result)
