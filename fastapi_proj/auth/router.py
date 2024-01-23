from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi_proj.auth.schemas import UserRequest
from fastapi_proj.auth.service import UserSerivce
from fastapi_proj.auth.config import ouath2_bearer


router = APIRouter(prefix="/account", tags=["/account"])


@router.post("/login")
async def account_login(
    service: Annotated[UserSerivce, Depends(UserSerivce)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    user = await service.authenticate_user(form_data.username, form_data.password)
    return user


@router.post("/register")
async def register_account(
    user: UserRequest, user_service: Annotated[UserSerivce, Depends(UserSerivce)]
):
    await user_service.add_user(user.username, user.password)
    return user


@router.get("/me")
async def get_account(token: Annotated[OAuth2PasswordBearer, Depends(ouath2_bearer)]):
    print(token)
