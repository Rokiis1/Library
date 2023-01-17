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
    except asyncpg.exceptions.UniqueViolationError as exc:
        raise HTTPException(status_code=400, detail="Username or email already taken") from exc
    except asyncpg.exceptions.NotNullViolationError as exc:
        raise HTTPException(status_code=400, detail="Missing required field")
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="An error occurred while registering the user"
        )
    finally:
        await conn.close()
