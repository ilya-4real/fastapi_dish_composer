from dataclasses import dataclass
from typing import Generic, TypeVar, Any
from domain.events.base import BaseEvent
from abc import ABC, abstractmethod

EventType = TypeVar("EventType", bound=BaseEvent)
EventResult = TypeVar("EventResult", bound=Any)


@dataclass
class BaseEventHandler(ABC, Generic[EventType, EventResult]):
    @abstractmethod
    def handle(self, event: EventType) -> EventResult:
        raise NotImplementedError
