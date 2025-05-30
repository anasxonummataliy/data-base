from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import AsyncGenerator

from app.config import settings

async_engine = create_async_engine(settings.db_url, echo=True)

SessionLocal = async_sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)