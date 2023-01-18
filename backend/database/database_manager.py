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


# async def create_table(conn):
#     try:
#         await conn.execute(
#             """
#             CREATE TABLE users (
#                 id SERIAL PRIMARY KEY,
#                 username VARCHAR(255) NOT NULL UNIQUE,
#                 email VARCHAR(255) NOT NULL UNIQUE,
#                 hashed_password VARCHAR(255) NOT NULL,
#                 is_active BOOLEAN DEFAULT true NOT NULL
#             );
#         """
#         )
#         conn.commit()
#         print("Table created successfully")
#     except Exception as e:
#         raise HTTPException(
#             status_code=500, detail=f"An error occurred while creating the table: {e}"
#         )
