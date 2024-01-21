from fastapi.middleware import Middleware


class AuthMiddleware(Middleware):
    @staticmethod
    async def jwt_generator():
        ...
