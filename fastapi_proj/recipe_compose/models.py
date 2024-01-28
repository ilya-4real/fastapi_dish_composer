from pydantic import BaseModel
from beanie import Document


class Ingredient(BaseModel):
    title: str
    amount: int


class ComponentDTO(BaseModel):
    title: str
    description: str
    ingredients: list[Ingredient]


class GarnishORM(Document, ComponentDTO):
    pass


class MeatORM(Document, ComponentDTO):
    pass


class SauceORM(Document, ComponentDTO):
    pass


class CompoundRecipe(BaseModel):
    garnish: GarnishORM
    meat: MeatORM
    sauce: SauceORM
