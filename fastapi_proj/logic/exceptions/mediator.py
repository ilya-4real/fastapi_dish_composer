from dataclasses import dataclass
from typing import Type

from fastapi_proj.domain.events.base import BaseEvent
from fastapi_proj.logic.comands.base import BaseCommand
from fastapi_proj.logic.exceptions.base import LogicException


@dataclass
class EventHandlerNotRegisteredError(LogicException):
    event_type: Type[BaseEvent]

    @property
    def message(self) -> str:
        return f"event of type {self.event_type} doesnt have any handler"


@dataclass
class CommandHandlerNotRegisteredError(LogicException):
    command_type: Type[BaseCommand]

    @property
    def message(self):
        return f"command of type{self.command_type} doesnt have any handler"
