import asyncpg
import pytest
from main import main, app

@pytest.mark.asyncio
async def test_main():
    conn = await main()
    assert isinstance(conn, asyncpg.pool.Pool)
    assert conn is not None

def test_app_router_included():
    assert app.router.routes