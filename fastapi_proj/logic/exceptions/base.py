from dataclasses import dataclass

from fastapi_proj.domain.exceptions.base import ApplicationException


@dataclass
class LogicException(ApplicationException):
    @property
    def message(self):
        return "a logic exception has been occured"
