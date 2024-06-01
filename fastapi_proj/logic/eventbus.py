from collections import defaultdict
from dataclasses import dataclass, field
from typing import Type

from fastapi_proj.domain.events.base import BaseEvent
from fastapi_proj.logic.events.base import BaseEventHandler


@dataclass
class EventBus:
    events_map: dict[Type[BaseEvent], list[BaseEventHandler]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    def register_event(
        self, event_type: Type[BaseEvent], handler: BaseEventHandler
    ):
        self.events_map[event_type].append(handler)

    def publish(self, events: list[BaseEvent]):
        for event in events:
            for handler in self.events_map[type(event)]:
                handler.handle(event)
