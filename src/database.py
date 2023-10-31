from typing import TYPE_CHECKING, AsyncGenerator, Optional

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker


if TYPE_CHECKING:
    from src.auth.models import User

DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

Base: DeclarativeMeta = declarative_base()


# class User(SQLAlchemyBaseUserTable[int], Base):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     hashed_password: Mapped[str] = mapped_column(nullable=False)
#     ggp_percent_begin: Mapped[int] = mapped_column(default=100, )
#     ggp_percent_end: Mapped[int] = mapped_column(default=150)
#     sub_ggp_percent: Mapped[int] = mapped_column(default=False)
#     sub_offline: Mapped[bool] = mapped_column(default=False)
#     sub_ggp: Mapped[bool] = mapped_column(default=False)
#     sub_world_record: Mapped[bool] = mapped_column(default=False)
#     telegram_id: Mapped[Optional[int]]
#     login: Mapped[Optional[str]]
#     email: Mapped[Optional[str]] = mapped_column(unique=True)
#     registered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
