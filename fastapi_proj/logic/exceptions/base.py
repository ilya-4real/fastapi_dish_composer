from dataclasses import dataclass

from fastapi_proj.domain.exceptions.base import ApplicationException


@dataclass
class LogicException(ApplicationException):
    msg: str

    @property
    def message(self) -> str:
        return "a logic exception has been occured"


@dataclass
class UserCannotUpdateRecipe(LogicException):
    @property
    def message(self) -> str:
        return f"{self.msg}"
