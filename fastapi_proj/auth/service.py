from fastapi import HTTPException, status
from fastapi_proj.auth.models import User
from fastapi_proj.auth.utils import (
    encrypt_password,
    verify_password,
    generate_jwt,
    decode_jwt,
)
from pymongo.errors import DuplicateKeyError


class UserSerivce:
    document = User

    async def add_user(self, username: str, password, email: str):
        hashed_password = encrypt_password(password)
        user = self.document(
            username=username, hashed_password=hashed_password, email=email
        )
        try:
            await user.insert()  # type: ignore
        except DuplicateKeyError:
            raise HTTPException(
                status.HTTP_409_CONFLICT, detail="username should be unique"
            )

    async def authenticate_user(self, username: str, password: str):
        user = await self.document.find({"username": username}).first_or_none()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="user is not authenticated",
            )
        if verify_password(password, user.hashed_password):
            return generate_jwt(user.username, str(user.id), 7 * 60)

    async def authenticate_by_token(self, token: str):
        decoded = decode_jwt(token)
        print(decoded)
        if not decoded:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="not authenticated"
            )
        found = await self.document.get(decoded.id)
        print(found)
        if not found:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="not authenticated"
            )
        return generate_jwt(decoded.username, decoded.id)
