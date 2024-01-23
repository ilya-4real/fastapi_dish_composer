import jwt
import datetime
from fastapi_proj.config import JWT_SECRET, JWT_ALGORITHM
from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_jwt(username: str, id: str, exp_in_seconds: int):
    if exp_in_seconds <= 0:
        return None
    payload = {"username": username, "id": id}
    exp_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(
        seconds=exp_in_seconds
    )
    payload["exp"] = exp_time  # type: ignore type
    return jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)


def check_jwt(token: str) -> dict[str, str | int] | None:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
        )
    except jwt.exceptions.PyJWTError:
        return None
    return payload


def encrypt_password(password: str):
    return crypt_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return crypt_context.verify(password, hashed_password)
