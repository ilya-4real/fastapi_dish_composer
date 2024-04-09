from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar


@dataclass(frozen=True)
class BaseCommand(ABC): ...


CommandType = TypeVar("CommandType", bound=BaseCommand)
CommandResult = TypeVar("CommandResult", bound=Any)


@dataclass
class BaseCommandHandler(ABC, Generic[CommandType, CommandResult]):
    @abstractmethod
    async def handle(self, command: CommandType) -> CommandResult:
        raise NotImplementedError
