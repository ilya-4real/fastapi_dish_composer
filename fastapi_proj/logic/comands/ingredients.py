from dataclasses import dataclass
from typing import Literal

from fastapi_proj.logic.comands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class CreateIngredientCommand(BaseCommand):
    title: str
    category: Literal["garnish", "sauce", "meat"]
    amount: int


@dataclass
class CreateIngredientCommandHandler(
    BaseCommandHandler[CreateIngredientCommand, str]
):
    async def handle(self, command): ...
