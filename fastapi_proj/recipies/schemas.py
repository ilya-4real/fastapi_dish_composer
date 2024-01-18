from pydantic import BaseModel


class Ingredient(BaseModel):
    title: str
    category: str


class RecipeDTO(BaseModel):
    title: str
    category: str
    description: str
    ingredients: list[Ingredient]
