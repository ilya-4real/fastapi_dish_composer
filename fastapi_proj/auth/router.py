from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi_proj.auth.schemas import UserRequest, Token, RefreshToken
from fastapi_proj.auth.service import UserSerivce


ouath2_bearer = OAuth2PasswordBearer(tokenUrl="account/token")


router = APIRouter(prefix="/account", tags=["/account"])


@router.post("/token", response_model=Token)
async def account_login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    token = await UserSerivce().authenticate_user(
        form_data.username, form_data.password
    )
    if token:
        return {"access_token": token, "token_type": "Bearer"}


@router.post("/refresh", response_model=RefreshToken)
async def get_refresh_token(
    service: Annotated[UserSerivce, Depends()],
    token: Annotated[str, Depends(ouath2_bearer)],
):
    new_token = await service.authenticate_by_token(token)
    if not new_token:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not authenticated"
        )
    return {"access_token": new_token, "token_type": "Bearer"}


@router.post("/register")
async def register_account(
    user: UserRequest, user_service: Annotated[UserSerivce, Depends(UserSerivce)]
):
    await user_service.add_user(user.username, user.password, user.email)
    return user


@router.get("/me")
async def get_account(token: Annotated[str, Depends(ouath2_bearer)]):
    ...
