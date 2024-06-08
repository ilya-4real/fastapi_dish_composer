from typing import Any

from fastapi_proj.domain.enteties.component import Component
from fastapi_proj.domain.enteties.recipe import Recipe


def convert_component_from_entity_to_document(
    component: Component,
) -> dict[str, Any]:
    data = {
        "oid": component.oid,
        "title": component.title.as_generic(),
        "category": component.category.name,
        "ingredients": [],
    }
    for ingredient in component.ingredients:
        data["ingredients"].append(
            {
                "title": ingredient.title.as_generic(),
                "amount": ingredient.amount.as_generic(),
            }
        )
    return data


def convert_recipe_to_document(recipe: Recipe) -> dict:
    document = {
        "oid": recipe.oid,
        "title": recipe.title,
        "author": recipe.author,
        "description": recipe.description,
        "components": [],
    }
    for component in recipe.components:
        document["components"].append(
            convert_component_from_entity_to_document(component)
        )
    return document
