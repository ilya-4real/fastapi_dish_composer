from pydantic import BaseModel


class UserRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# class TokenData(BaseModel):
#     username: str
#     scopes: list[str] = []
