from pydantic_settings import Base

class Settings(Base):
    db_url : str = "sqlite + aiosqlite:///./regis.db"

settings = Settings()