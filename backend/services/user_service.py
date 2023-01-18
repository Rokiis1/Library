import asyncpg
import bcrypt
from fastapi import HTTPException
from models.user import User
from database import database_manager


async def register(user: User):
    try:
        conn = await database_manager.get_connection()
        hashed_password = bcrypt.hashpw(user.hashed_password.encode(), bcrypt.gensalt())
        query = f"INSERT INTO users (username, email, hashed_password, is_active) VALUES ('{user.username}', '{user.email}', '{hashed_password.decode()}', {user.is_active})"
        await conn.execute(query)
        return {"message": "User registered successfully"}
    except asyncpg.exceptions.UniqueViolationError as e:
        raise HTTPException(
            status_code=400, detail="Username or email already taken"
        ) from e
    except asyncpg.exceptions.NotNullViolationError as exc:
        raise HTTPException(status_code=400, detail="Missing required field") from exc
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="An error occurred while registering the user"
        ) from e
    finally:
        await conn.close()
        
async def login(user: User):
    conn = await database_manager.get_connection()
    try:
        query = f"SELECT * FROM users WHERE email='{user.email}'"
        result = await conn.fetchrow(query)
        if not result:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        hashed_password = result['hashed_password']
        if bcrypt.checkpw(user.hashed_password.encode(), hashed_password.encode()):
            return {"message": "Logged in successfully"}
        else:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while logging in") from e
    finally:
        await conn.close()
