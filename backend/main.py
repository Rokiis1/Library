import asyncio
import uvicorn
from fastapi import FastAPI
from database.database_manager import create_table, get_connection
from routes.api import router

app = FastAPI()

async def main():
    try:
        conn = await get_connection()
        print("Successfully connected to the database.")
    except Exception as e:
        print(f"Error: {e}")
    return conn

app.include_router(router)

if __name__ == "__main__":
    conn = asyncio.run(main())
    uvicorn.run(app, port=8080)
