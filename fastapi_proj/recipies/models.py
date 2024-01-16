from typing import Annotated
from pydantic import BaseModel
from beanie import Document, Indexed
import pymongo


class Ingredient(BaseModel):
    title: Annotated[str, Indexed(str, unique=True)]
    category: str


class Recipe(Document):
    title: Annotated[str, Indexed(str, unique=True)]
    category: str
    description: str
    ingredients: list[Ingredient]
    