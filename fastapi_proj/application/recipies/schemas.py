from pydantic import BaseModel, ConfigDict


class RecipeLikeSchema(BaseModel):
    author_id: str


class RecipeResponceSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")
    oid: str
    author: str
    title: str
    description: str
    likes: int


class SearchRecipeSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")
    oid: str
    title: str


class RecipesResponceSchema(BaseModel):
    recipes: list[RecipeResponceSchema]


class SearchRecipesSchema(BaseModel):
    recipes: list[SearchRecipeSchema]
