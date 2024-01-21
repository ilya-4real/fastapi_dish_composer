import jwt
import datetime
from fastapi_proj.config import JWT_SECRET, JWT_ALGORITHM
from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_jwt(username: str, id: str, exp_in_seconds: int):
    payload = {"username": username, "id": id}
    exp_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(
        seconds=exp_in_seconds
    )
    payload["exp"] = exp_time  # type: ignore
    return jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)


def check_jwt(token: str):
    payload = jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[JWT_ALGORITHM],
    )
    username = payload.get("username")
    id = payload.get("id")
    if username is None or id is None:
        return None
    return


def encrypt_password(password: str):
    return crypt_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return crypt_context.verify(password, hashed_password)
