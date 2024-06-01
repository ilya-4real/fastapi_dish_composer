from dataclasses import dataclass

from fastapi_proj.domain.exceptions.ingredients import (
    IngredientAmountTooLow,
    IngredientNameTooLongException,
)
from fastapi_proj.domain.values.base import BaseValueObject


@dataclass
class CommonTitle[str](BaseValueObject):
    def validate(self) -> None:
        if len(self.value) == 0 or len(self.value) >= 100:
            raise IngredientNameTooLongException(400, self.value)

    def as_generic(self) -> str:
        return self.value


@dataclass
class IngredientAmount[int](BaseValueObject):
    def validate(self) -> None:
        if self.value <= 0:
            raise IngredientAmountTooLow(400, self.value)

    def as_generic(self) -> int:
        return self.value
