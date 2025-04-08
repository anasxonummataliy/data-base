from fastapi import APIRouter

router = APIRouter(
    prefix="/registration",
    tags="[Registration]"
)

@router.get("/")
async def regis():
    pass