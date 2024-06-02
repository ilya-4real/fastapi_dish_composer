from dataclasses import dataclass
from enum import Enum

from fastapi_proj.domain.enteties.base import BaseEntity
from fastapi_proj.domain.values.components import (
    CommonTitle,
    IngredientAmount,
)


class ComponentCategory(str, Enum):
    meat = "meat"
    garnish = "garnish"
    sauce = "sauce"


@dataclass
class Ingredient:
    title: CommonTitle
    amount: IngredientAmount


@dataclass
class Component(BaseEntity):
    title: CommonTitle
    category: ComponentCategory
    ingredients: list[Ingredient]

    def add_ingredient(
        self,
        ingredient: Ingredient,
    ) -> None:
        self.ingredients.append(ingredient)
