from fastapi import HTTPException
import asyncpg


async def get_connection():
    try:
        conn = await asyncpg.create_pool(
            host="db.uzfyszuaseakoacmgvpt.supabase.co",
            database="postgres",
            port="5432",
            user="postgres",
            password="GdX1ZhGsBV0h68Cu",
        )
        return conn
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while connecting to the database: {e}",
        ) from e


def close_connection(conn):
    conn.close()
