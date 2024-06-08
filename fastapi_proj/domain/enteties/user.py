from dataclasses import dataclass, field

from fastapi_proj.domain.enteties.base import BaseEntity


@dataclass
class User(BaseEntity):
    username: str
    liked_recipes: list[str] = field(default_factory=list)
    created_recipes: list[str] = field(default_factory=list)

    def like_recipe(self, recipe_id: str) -> None:
        self.liked_recipes.append(recipe_id)

    def unlike_recipe(self, recipe_id: str) -> None:
        self.liked_recipes.remove(recipe_id)

    def add_own_recipe(self, recipe_id: str) -> None:
        self.created_recipes.append(recipe_id)
