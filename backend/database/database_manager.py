from fastapi import HTTPException
import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()

async def get_connection():
    try:
        conn = await asyncpg.create_pool(
            host=os.getenv("DATABASE_HOST"),
            database=os.getenv("DATABASE_NAME"),
            port=os.getenv("DATABASE_PORT"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
        )
        return conn
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while connecting to the database: {e}",
        ) from e


def close_connection(conn):
    conn.close()
