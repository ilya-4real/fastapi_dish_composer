from pydantic import BaseModel, ConfigDict, Field


class Ingredient(BaseModel):
    title: str
    amount: int = Field(gt=1)


class Component(BaseModel):
    title: str = Field(min_length=2)
    ingredients: list[Ingredient]


class CreateRecipeSchema(BaseModel):
    author: str = Field(min_length=2)
    title: str = Field(min_length=2, max_length=100)
    description: str
    components: list[Component]


class UpdateRecipeSchema(BaseModel):
    title: str = Field(min_length=2)
    description: str
    components: list[Component]


class RecipeResponceSchema(CreateRecipeSchema):
    model_config = ConfigDict(extra="ignore")
    is_liked: bool = False
    oid: str | None = None
    likes: int


class RecipesResponceSchema(BaseModel):
    recipes: list[RecipeResponceSchema]
