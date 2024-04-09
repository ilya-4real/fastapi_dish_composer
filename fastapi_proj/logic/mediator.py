from collections import defaultdict
from dataclasses import dataclass, field
from typing import Generic, Iterable, Type

from fastapi_proj.domain.events.base import BaseEvent
from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler
from fastapi_proj.logic.events.base import BaseEventHandler
from fastapi_proj.logic.exceptions.mediator import (
    CommandHandlerNotRegisteredError,
    EventHandlerNotRegisteredError,
)


@dataclass(eq=False)
class Mediator:
    events_map: dict[Type[BaseEvent], list[BaseEventHandler]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )
    commands_map: dict[Type[BaseCommand], list[BaseCommandHandler]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    def register_event(
        self, event: BaseEvent, handlers: Iterable[BaseEventHandler]
    ) -> None:
        self.events_map[event.__class__].extend(handlers)

    def register_command(
        self, command: BaseCommand, handlers: Iterable[BaseCommandHandler]
    ) -> None:
        self.commands_map[command.__class__].extend(handlers)

    def publish_event(self, event: BaseEvent):
        event_type = type(event)
        handlers = self.events_map.get(event_type)

        if not handlers:
            raise EventHandlerNotRegisteredError(500, event_type)

        return [await handler.handle(event) for handler in handlers]

    async def handle_command(self, command: BaseCommand):
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlerNotRegisteredError(500, command_type)

        return [await handler.handle(command) for handler in handlers]
