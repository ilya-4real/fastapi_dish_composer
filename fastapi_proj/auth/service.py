from fastapi import HTTPException, status
from fastapi_proj.auth.models import User
from fastapi_proj.auth.utils import encrypt_password
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

    async def authenticate_user(self, username: str, password):
        ...
