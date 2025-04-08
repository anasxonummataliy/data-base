from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.regis import router as regis_router

@asynccontextmanager
async def lifespan(app : FastAPI):
    pass


app = FastAPI(
    title="Auth API",
    description="Auth API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(regis_router)
