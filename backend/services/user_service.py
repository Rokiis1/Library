import asyncpg
import bcrypt
from fastapi import HTTPException
import jwt
from models.user import User
from database import database_manager


async def register(user: User):
    try:
        conn = await database_manager.get_connection()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occurred while connecting to the database")
    try:
        hashed_password = bcrypt.hashpw(user.hashed_password.encode(), bcrypt.gensalt())
        query = f"INSERT INTO users (username, email, hashed_password, is_active) VALUES ('{user.username}', '{user.email}', '{hashed_password.decode()}', {user.is_active})"
        await conn.execute(query)
        return {"message": "User registered successfully"}
    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Username or email already taken")
    except asyncpg.exceptions.NotNullViolationError:
        raise HTTPException(status_code=400, detail="Missing required field")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occurred while registering the user")
    finally:
        await conn.close()

async def login(user: User):
    conn = database_manager.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT hashed_password FROM users WHERE username = %s", (user.username,))
    stored_password = cur.fetchone()[0]
    if not bcrypt.verify(user.hashed_password, stored_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    encoded_jwt = jwt.encode({"sub": user.username}, "secret", algorithm="HS256")
    cur.close()
    return {"access_token": encoded_jwt}
