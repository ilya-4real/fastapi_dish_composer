from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import Any, TypeVar

VT = TypeVar("VT", bound=Any)


@dataclass
class BaseValueObject[VT](ABC):
    value: VT

    def __post_init__(self) -> None:
        self.validate()

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def as_generic(self) -> VT:
        raise NotImplementedError
