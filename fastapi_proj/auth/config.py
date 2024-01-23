from fastapi.security import OAuth2PasswordBearer

ouath2_bearer = OAuth2PasswordBearer(tokenUrl="account/login")
