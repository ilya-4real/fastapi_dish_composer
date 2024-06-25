from typing import Any

from fastapi_proj.domain.enteties.component import (
    Component,
    ComponentCategory,
    Ingredient,
)
from fastapi_proj.domain.values.components import CommonTitle, IngredientAmount


def convert_dict_to_components(comps: list[dict[str, Any]]) -> list[Component]:
    components: list[Component] = []
    for component in comps:
        ingredients: list[Ingredient] = []
        for ingredient in component["ingredients"]:
            ingr = Ingredient(
                CommonTitle(ingredient["title"]), IngredientAmount(ingredient["amount"])
            )
            ingredients.append(ingr)
        components.append(
            Component(
                CommonTitle(component["title"]), ComponentCategory("none"), ingredients
            )
        )

    return components
