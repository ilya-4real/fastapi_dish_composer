from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable, Type

from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler
from fastapi_proj.logic.exceptions.mediator import (
    CommandHandlerNotRegisteredError,
)


@dataclass(eq=False)
class Mediator:
    commands_map: dict[Type[BaseCommand], list[BaseCommandHandler]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    def register_command(
        self,
        command: Type[BaseCommand],
        handlers: Iterable[BaseCommandHandler],
    ) -> None:
        self.commands_map[command].extend(handlers)

    async def handle_command(self, command: BaseCommand):
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlerNotRegisteredError(500, command_type)

        return [await handler.handle(command) for handler in handlers]
