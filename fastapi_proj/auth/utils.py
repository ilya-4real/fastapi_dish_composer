from collections import namedtuple
from jose import jwt, JWTError
import datetime
from fastapi_proj.config import JWT_SECRET, JWT_ALGORITHM
from passlib.context import CryptContext
from time import time

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

TokenPayload = namedtuple("TokenPayload", "username id exp_time")


def generate_jwt(username: str, id: str, exp_in_seconds: int = 20 * 60):
    if exp_in_seconds <= 0:
        return None
    payload = {"username": username, "id": id}
    exp_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(
        seconds=exp_in_seconds
    )
    payload["exp"] = exp_time  # type: ignore type
    return jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)


def decode_jwt(token: str) -> TokenPayload | None:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
        )
    except JWTError:
        return None
    exp_time = payload["exp"]
    if exp_time >= time():
        return TokenPayload(payload["username"], payload["id"], payload["exp"])


def encrypt_password(password: str):
    return crypt_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return crypt_context.verify(password, hashed_password)
