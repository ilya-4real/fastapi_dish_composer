from pydantic import BaseModel, ConfigDict, Field

from fastapi_proj.domain.enteties.component import ComponentCategory


class Ingredient(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    amount: int = Field(ge=1)


class CreateComponentShema(BaseModel):
    title: str = Field(min_length=2, max_length=120)
    component_category: ComponentCategory
    ingredients: list[Ingredient]


class ComponentResponceSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")
    oid: str
    title: str = Field(min_length=2, max_length=100)
    category: ComponentCategory
    ingredients: list[Ingredient]


class ListOfComponentsResponceSchema(BaseModel):
    components: list[ComponentResponceSchema]


class UpdateComponentSchema(BaseModel):
    ingredients: list[Ingredient]
