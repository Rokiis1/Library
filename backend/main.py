import uvicorn
from fastapi import FastAPI
from database.database_manager import create_table, get_connection
from routes.api import router

app = FastAPI()

try:
    conn = get_connection()
    print("Successfully connected to the database.")
except Exception as e:
    print(f"Error: {e}")

app.include_router(router)

if __name__ == "__main__":
    conn = get_connection()
    # create_table(conn)
    uvicorn.run(app, port=8080)
