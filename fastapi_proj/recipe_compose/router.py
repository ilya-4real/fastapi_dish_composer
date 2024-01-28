from fastapi import APIRouter
from fastapi_proj.recipe_compose import models


router = APIRouter(prefix="/components", tags=["components"])


@router.get("/compose", response_model=models.CompoundRecipe)
async def compose_recipe():
    garnish = await models.GarnishORM.aggregate(
        [{"$sample": {"size": 1}}], projection_model=models.GarnishORM
    ).to_list()
    meat = await models.MeatORM.aggregate(
        [{"$sample": {"size": 1}}], projection_model=models.MeatORM
    ).to_list()
    sauce = await models.SauceORM.aggregate(
        [{"$sample": {"size": 1}}], projection_model=models.SauceORM
    ).to_list()
    return {"garnish": garnish[0], "meat": meat[0], "sauce": sauce[0]}


@router.post("/garnish/add")
async def add_garnish(garnish: models.ComponentDTO):
    print(garnish.model_dump())
    new_garnish = models.GarnishORM(**garnish.model_dump())
    await new_garnish.insert()  # type: ignore


@router.post("/meat/add")
async def add_meat(meat: models.ComponentDTO):
    new_meat = models.MeatORM(**meat.model_dump())
    await new_meat.insert()  # type: ignore


@router.post("/sauce/add")
async def add_sauce(sauce: models.ComponentDTO):
    new_sauce = models.SauceORM(**sauce.model_dump())
    await new_sauce.insert()  # type: ignore
