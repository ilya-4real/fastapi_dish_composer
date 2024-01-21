from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import APIKeyCookie
from fastapi_proj.auth.utils import generate_jwt
from fastapi_proj.auth.schemas import UserRequest
from fastapi_proj.auth.service import UserSerivce


router = APIRouter(prefix="/account", tags=["/account"])


@router.post("/login")
async def account_login(
    user: UserRequest, service: Annotated[UserSerivce, Depends(UserSerivce)]
):
    ...


@router.post("/register")
async def register_account(
    user: UserRequest, user_service: Annotated[UserSerivce, Depends(UserSerivce)]
):
    await user_service.add_user(user.username, user.password)
    return user
