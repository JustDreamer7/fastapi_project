import os

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm  import DeclarativeBase
from app.config import settings

if settings.MODE == "TEST":
    DB_URL = settings.DB_URL
    DB_PARAMS = {"poolclass": NullPool}
else:
    DB_URL = settings.DB_URL
    DB_PARAMS = {}

engine = create_async_engine(DB_URL, **DB_PARAMS)
engine_nullpool = create_async_engine(DB_URL, poolclass=NullPool)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
async_session_maker_nullpool = async_sessionmaker(engine_nullpool, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
