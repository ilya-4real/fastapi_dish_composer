from typing import Annotated
from pydantic import BaseModel
from beanie import Document, Indexed
from fastapi_proj.recipies.schemas import Ingredient


class Recipe(Document):
    title: Annotated[str, Indexed(str, unique=True)]
    category: str
    description: str
    ingredients: list[Ingredient]
    