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
        cur = await conn.cursor()
        hashed_password = bcrypt.hashpw(user.hashed_password.encode(), bcrypt.gensalt())
        query = f"INSERT INTO users (username, email, hashed_password, is_active) VALUES ('{user.username}', '{user.email}', '{hashed_password.decode()}', {user.is_active})"
        try:
            await cur.execute(query)
            await conn.commit()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="An error occurred while executing the query")
        return {"message": "User registered successfully"}
    except Exception as e:
        if "duplicate key value violates unique constraint" in str(e):
            raise HTTPException(
                status_code=400, detail="Username or email already taken"
            )
        elif "null value in column" in str(e):
            raise HTTPException(status_code=400, detail="Missing required field")
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while registering the user"
            )


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
