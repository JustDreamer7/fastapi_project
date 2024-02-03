import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm  import DeclarativeBase
from app.config import settings

DB_URL = settings.DB_URL
engine = create_async_engine(DB_URL)
# with engine.connect() as connection: # Не работает с AsyncSession
#     connection.execute(f'CREATE DATABASE {os.environ.get("db_name")}')
# conn = engine.connect() # Просто не работает
# conn.execute("commit")
# conn.execute(f'CREATE DATABASE {os.environ.get("db_name")}')
# conn.close()
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
