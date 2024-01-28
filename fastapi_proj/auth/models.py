from typing import Annotated
from pydantic import BaseModel, EmailStr, Field
from beanie import Document, Indexed


class UserDTO(BaseModel):
    username: str
    email: Annotated[EmailStr, Indexed(unique=True)]


class User(Document, UserDTO):
    disabled: bool = Field(default=False)
    hashed_password: str

    def __repr__(self) -> str:
        return f"{self.username}"
