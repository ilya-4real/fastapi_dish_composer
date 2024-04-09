from dataclasses import dataclass, field
from typing import Literal

from fastapi_proj.domain.enteties.base import BaseEntity


@dataclass
class Ingredient(BaseEntity):
    title: str
    category: Literal["garnish", "sauce", "meat"]
    amount: int


@dataclass
class Recipe(BaseEntity):
    title: str = field(kw_only=True)
    category: str = field(kw_only=True)
    description: str = field(kw_only=True)
    ingredients: list[Ingredient] = field(default_factory=list)
