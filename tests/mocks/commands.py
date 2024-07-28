from dataclasses import dataclass

from polyfactory.factories import DataclassFactory

from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class DummyCommand(BaseCommand):
    command_text: str


@dataclass
class DummyCommandHandler(BaseCommandHandler[DummyCommand, str]):
    async def handle(self, command: DummyCommand) -> str:
        return command.command_text


class DummyCommandFactory(DataclassFactory[DummyCommand]):
    __model__ = DummyCommand
