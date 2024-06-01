from dataclasses import dataclass, field
from enum import Enum

from fastapi_proj.domain.enteties.base import BaseEntity
from fastapi_proj.domain.values.ingredient import (
    CommonTitle,
    IngredientAmount,
)


class ComponentCategory(Enum):
    meat = 1
    garnish = 2
    sauce = 3


@dataclass
class Component(BaseEntity):
    title: CommonTitle
    category: ComponentCategory
    ingredients: dict[CommonTitle, IngredientAmount] = field(init=False)

    def add_ingredient(
        self, ingredient: CommonTitle, amount: IngredientAmount
    ) -> None:
        self.ingredients[ingredient] = amount
