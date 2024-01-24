from typing import Annotated
from fastapi import Depends
from fastapi_proj.auth.utils import decode_jwt


# def get_user(token: Annotated[str, Depends(ouath2_bearer)]):
#     print(token)
#     user_dict = decode_jwt(token)
#     if user_dict:
#         return user_dict
