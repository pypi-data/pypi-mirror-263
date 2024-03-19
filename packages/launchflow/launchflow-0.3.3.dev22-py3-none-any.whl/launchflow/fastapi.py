try:
    from sqlalchemy import Engine
    from sqlalchemy.orm import Session, sessionmaker
except ImportError:
    Session = None
    Engine = None
    sessionmaker = None


try:
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
except ImportError:
    AsyncSession = None
    AsyncEngine = None
    async_sessionmaker = None


class _AsyncSQLAlchemyDep:
    def __init__(
        self,
        expire_on_commit: bool,
        autoflush: bool,
    ):
        self.expire_on_commit = expire_on_commit
        self.autoflush = autoflush

    def initialize(self, engine):
        self.engine = engine
        self._SessionLocal = async_sessionmaker(
            expire_on_commit=self.expire_on_commit,
            autoflush=self.autoflush,
            bind=engine,
        )

    async def __call__(self):
        async with self._SessionLocal() as db:
            yield db


class _SQLAlchemyDep:
    def __init__(
        self,
        engine,
        expire_on_commit: bool,
        autoflush: bool,
    ):
        self.engine = engine
        self._SessionLocal = sessionmaker(
            expire_on_commit=expire_on_commit, autoflush=autoflush, bind=engine
        )

    def __call__(self):
        with self._SessionLocal() as db:
            yield db


def sqlalchemy(engine: Engine, expire_on_commit: bool = False, autoflush: bool = False):
    """Returns a dependency that returns a SQLAlchemy session for use in FastAPI.

    Args:
    - `engine`: A SQLAlchemy engine to use for creating the session.
    - `expire_on_commit`: Whether to expire all instances after a commit.
    - `autoflush`: Whether to autoflush the session after a commit.

    Example usage:
    ```python
    from fastapi import FastAPI, Depends
    import launchflow
    from sqlalchemy import text

    db = launchflow.gcp.CloudSQLPostgres("my-pg-db")
    engine = db.sqlalchemy_engine()
    get_db = launchflow.fastapi.sqlalchemy(engine)

    app = FastAPI()

    @app.get("/")
    def read_root(db: Session = Depends(get_db)):
        return db.execute(text("SELECT 1")).scalar_one_or_none()
    ```
    """
    if Session is None or sessionmaker is None:
        raise ImportError(
            "Requires `sqlalchemy` library, which is not installed. Install with `pip install sqlalchemy`."
        )
    return _SQLAlchemyDep(
        engine, expire_on_commit=expire_on_commit, autoflush=autoflush
    )


def sqlalchemy_async(expire_on_commit: bool = False, autoflush: bool = False):
    if AsyncSession is None or async_sessionmaker is None:
        raise ImportError(
            "Requires `sqlalchemy` library, which is not installed. Install with `pip install sqlalchemy[asyncio]`."
        )
    return _AsyncSQLAlchemyDep(expire_on_commit=expire_on_commit, autoflush=autoflush)
