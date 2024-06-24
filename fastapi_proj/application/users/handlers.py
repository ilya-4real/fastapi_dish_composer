from logging import getLogger
from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi_proj.application.dependencies import (
    get_query_mediator,
    get_user,
)
from fastapi_proj.application.schemas import RecipesResponceSchema
from fastapi_proj.domain.enteties.user import User
from fastapi_proj.logic.queries.users import (
    GetUserCreatedRecipesQuery,
    GetUserLikedRecipesQuery,
)
from fastapi_proj.logic.querymediator import QueryMediator

logger = getLogger(__name__)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/recipes")
async def get_users_recipes(
    user: Annotated[User, Depends(get_user)],
    mediator: Annotated[QueryMediator, Depends(get_query_mediator)],
):
    logger.debug(user)
    query = GetUserCreatedRecipesQuery(user.username)
    result = await mediator.handle_query(query)
    logger.debug(result)
    logger.debug(type(result))
    return RecipesResponceSchema.model_validate(result)


@router.get("/liked")
async def get_users_liked_recipes(
    user: Annotated[User, Depends(get_user)],
    mediator: Annotated[QueryMediator, Depends(get_query_mediator)],
):
    query = GetUserLikedRecipesQuery(user.username)
    result = await mediator.handle_query(query)
    return RecipesResponceSchema.model_validate(result)
