from dataclasses import dataclass

from fastapi_proj.domain.exceptions.base import ApplicationException


@dataclass
class DuplicateComponentException(ApplicationException):
    @property
    def message(self):
        return "component name should be unique"


@dataclass
class IngredientNameTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f"ingredient name is too long: {self.text}"


@dataclass
class IngredientAmountTooLow(ApplicationException):
    amount: int

    @property
    def message(self):
        return f"ingredient amount must be greater than 1: {self.amount}"
