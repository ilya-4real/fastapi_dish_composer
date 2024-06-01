from fastapi import APIRouter

router = APIRouter(prefix="/components", tags=["components"])


@router.post("")
async def create_ingredient(): ...


@router.get("")
async def get_all_ingredients(): ...


@router.get("{ingredient_name}")
async def get_one_ingredient_by_id(ingredient_name: str): ...


@router.put("{ingredient_name}")
async def change_ingredient(ingredient_name: str): ...
