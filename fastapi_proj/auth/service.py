from fastapi import HTTPException, status
from fastapi_proj.auth.models import User
from fastapi_proj.auth.utils import encrypt_password, verify_password, generate_jwt
from pymongo.errors import DuplicateKeyError


class UserSerivce:
    document = User

    async def add_user(self, username: str, password):
        hashed_password = encrypt_password(password)
        user = self.document(username=username, hashed_password=hashed_password)
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
            return generate_jwt(user.username, "13242afd2", 7 * 60)
