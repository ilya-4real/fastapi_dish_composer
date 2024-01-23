from typing import Annotated
from pydantic import BaseModel, EmailStr, Field
from beanie import Document, Indexed


class UserDTO(BaseModel):
    username: Annotated[str, Indexed(unique=True)]
    email: EmailStr | None = None


class User(Document, UserDTO):
    disabled: bool = Field(default=False)
    hashed_password: str
