import logging
from contextlib import asynccontextmanager

from psycopg import AsyncConnection
from psycopg.rows import TupleRow

logger = logging.getLogger(__name__)


async def fetch_databases() -> list[str]:
    query = """
    SELECT datname
    FROM pg_database
    WHERE datallowconn AND NOT datistemplate;
    """

    rows = await select(query)
    return [r[0] for r in rows]


async def select(query: str) -> list[TupleRow]:
    async with execute(query) as cursor:
        return await cursor.fetchall()


@asynccontextmanager
async def execute(query: str):
    logger.info(f"Running query: {query}")
    async with connect() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(query.encode())
            yield cursor


@asynccontextmanager
async def connect():
    conn = await AsyncConnection.connect()
    async with conn:
        yield conn
