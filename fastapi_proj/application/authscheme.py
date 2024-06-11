from typing import Any

from fastapi import HTTPException, Request, status
from fastapi.openapi.models import OAuthFlows
from fastapi.security.oauth2 import OAuth2


class NickNameAuth(OAuth2):
    def __init__(
        self,
        *,
        flows: OAuthFlows | dict[str, dict[str, Any]] = OAuthFlows(),
        scheme_name: str | None = None,
        description: str | None = None,
        auto_error: bool = True,
    ):
        super().__init__(
            flows=flows,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error,
        )

    async def __call__(self, request: Request) -> str | None:
        authorization = request.headers.get("Authorization")
        if not authorization and self.auto_error:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "unauthorized")
        return authorization


auth_scheme = NickNameAuth()
