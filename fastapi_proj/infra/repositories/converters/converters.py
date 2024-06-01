from typing import Any

from fastapi_proj.domain.enteties.component import Component


def convert_component_from_entity_to_document(
    component: Component,
) -> dict[str, Any]:
    return {
        "title": component.title,
        "category": component.category.name,
        "ingredients": component.ingredients,
    }
