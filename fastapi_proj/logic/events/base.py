from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from fastapi_proj.domain.events.base import BaseEvent
from fastapi_proj.logic.eventbus import EventBus

EventType = TypeVar("EventType", bound=BaseEvent)
EventResult = TypeVar("EventResult", bound=Any)


@dataclass
class BaseEventHandler(ABC, Generic[EventType, EventResult]):
    event_bus: EventBus

    @abstractmethod
    def handle(self, event: EventType) -> EventResult:
        raise NotImplementedError
