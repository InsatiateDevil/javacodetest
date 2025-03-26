from asyncio import current_task

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, \
    async_scoped_session

from src.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            pool_size=20,
            pool_recycle=20,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def get_db_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        yield session
        await session.close()


db_helper = DatabaseHelper(
    settings.db_url,
    echo=settings.db_echo,
)
