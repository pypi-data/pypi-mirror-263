# Handling imports and missing dependencies
try:
    import boto3
except ImportError:
    boto3 = None

try:
    import asyncpg
except ImportError:
    asyncpg = None

try:
    import pg8000
except ImportError:
    pg8000 = None

try:
    from sqlalchemy.ext.asyncio import create_async_engine
except ImportError:
    async_sessionmaker = None
    create_async_engine = None

try:
    from sqlalchemy import create_engine, event
except ImportError:
    event = None
    create_engine = None
    DeclarativeBase = None
    sessionmaker = None

# Importing the required modules

from launchflow.resource import Resource
from pydantic import BaseModel


# Connection information model
class RDSPostgresConnectionInfo(BaseModel):
    # TODO: remove this and get it from the bucket
    endpoint: str = "caleb-aws-testing-dev-my-pg-db-postgres-cluster.cluster-cbm0kk2gelr2.us-east-1.rds.amazonaws.com"
    username: str
    password: str
    port: str = "5432"
    dbname: str = "Mypgdb"
    region: str = "us-east-1"


class RDSPostgres(Resource[RDSPostgresConnectionInfo]):
    """A RDS SQL Postgres resource.

    Args:
    - `name`: The name of the Cloud SQL Postgres instance.

    Example usage:
    ```python
    import launchflow as lf
    db = lf.aws.RDSPostgres("my-pg-db")
    ```
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        super().__init__(
            name=name,
            product_name="aws_rds_postgres",
            create_args={},
        )

    def sqlalchemy_engine(self, **engine_kwargs):
        """Returns a SQLAlchemy engine for connecting to the RDS SQL Postgres instance.

        Args:
        - `**engine_kwargs`: Additional keyword arguments to pass to `sqlalchemy.create_engine`.

        Example usage:
        ```python
        import launchflow as lf
        db = lf.aws.RDSPostgres("my-pg-db")
        db.connect()
        engine = db.sqlalchemy_engine()
        ```
        """
        if create_engine is None:
            raise ImportError(
                "SQLAlchemy is not installed. Please install it with "
                "`pip install sqlalchemy`."
            )
        if pg8000 is None:
            raise ImportError(
                "pg8000 is not installed. Please install it with `pip install pg8000`."
            )
        connection_info = self.connect()

        return create_engine(
            f"postgresql+pg8000://{connection_info.username}:{connection_info.password}@{connection_info.endpoint}:{connection_info.port}/{connection_info.dbname}"
        )

    async def sqlalchemy_async_engine(self, **engine_kwargs):
        """Returns an async SQLAlchemy engine for connecting to the RDS SQL Postgres instance.

        Args:
        - `**engine_kwargs`: Additional keyword arguments to pass to `create_async_engine`.

        Example usage:
        ```python
        import launchflow as lf
        db = lf.aws.RDSPostgres("my-pg-db")
        await db.connect_async()
        engine = await db.sqlalchemy_async_engine()
        ```
        """
        if create_async_engine is None:
            raise ImportError(
                "SQLAlchemy asyncio extension is not installed. "
                "Please install it with `pip install sqlalchemy[asyncio]`."
            )
        if asyncpg is None:
            raise ImportError(
                "asyncpg is not installed. Please install it with `pip install asyncpg`."
            )
        connection_info = await self.connect_async()
        connection_string = f"postgresql+asyncpg://{connection_info.endpoint}:{connection_info.password}@{connection_info.username}:{connection_info.port}/{connection_info.dbname}"
        return create_async_engine(connection_string, **engine_kwargs)
