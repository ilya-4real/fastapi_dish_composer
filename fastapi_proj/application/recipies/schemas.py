from pydantic import BaseModel, Field


class Compound(BaseModel):
    title: str = Field(min_length=2)
    amount: int = Field(gt=1)


class CreateRecipeSchema(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str
    compounds: list[Compound]
