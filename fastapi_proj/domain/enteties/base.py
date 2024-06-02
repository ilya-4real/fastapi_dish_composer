from abc import ABC
from copy import copy
from dataclasses import dataclass, field
from uuid import uuid4

from fastapi_proj.domain.events.base import BaseEvent


@dataclass
class BaseEntity(ABC):
    oid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    _events: list[BaseEvent] = field(default_factory=list, kw_only=True)

    def register_event(self, event: BaseEvent):
        self._events.append(event)

    def pull_events(self):
        registered_events = copy(self._events)
        self._events.clear()
        return registered_events
