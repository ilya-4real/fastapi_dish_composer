from typing import Any

from fastapi_proj.domain.enteties.component import Component


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
