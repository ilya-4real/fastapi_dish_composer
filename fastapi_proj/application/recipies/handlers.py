from fastapi import APIRouter

router = APIRouter(prefix="/recipies", tags=["recipies"])


@router.get("/random")
async def generate_random_recipe(): ...
