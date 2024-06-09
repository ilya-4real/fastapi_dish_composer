from pydantic import BaseModel, ConfigDict


class RecipeLikeSchema(BaseModel):
    author_id: str


class QueryRecipeSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")
    oid: str
    author: str
    title: str
    description: str
    likes: int


class QueryRecipesSchema(BaseModel):
    recipes: list[QueryRecipeSchema]
