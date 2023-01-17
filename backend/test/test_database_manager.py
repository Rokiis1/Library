import asyncpg
import pytest
from database.database_manager import get_connection

async def close_connection(conn):
    await conn.close()

@pytest.mark.asyncio
async def test_get_connection():
    conn = await get_connection()
    assert isinstance(conn, asyncpg.pool.Pool)
    await close_connection(conn)