from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv

import os

load_dotenv()


async_engine = create_async_engine(os.getenv("DB_URL"))
async_session_maker = async_sessionmaker(
    bind=async_engine, expire_on_commit=False, class_=AsyncSession
)


class Base(DeclarativeBase):
    pass
