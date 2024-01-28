from typing import Annotated
from pydantic import BaseModel
from beanie import Document, Indexed


class Ingredient(BaseModel):
    title: str
    category: str


class RecipeDTO(BaseModel):
    title: Annotated[str, Indexed(str, unique=True)]
    category: str | None = None
    description: str | None = None
    ingredients: list[Ingredient] | None = None


class Recipe(Document, RecipeDTO):
    pass
