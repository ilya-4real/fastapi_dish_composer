from typing import Annotated
from pydantic import BaseModel, EmailStr
from beanie import Document, Indexed


class UserModel(BaseModel):
    username: Annotated[str, Indexed(unique=True)]
    hashed_password: str
    email: EmailStr | None = None


class User(Document, UserModel):
    pass
