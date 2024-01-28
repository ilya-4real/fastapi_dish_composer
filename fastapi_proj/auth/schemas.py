from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    username: str
    password: str
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class RefreshToken(BaseModel):
    access_token: str
    token_type: str
