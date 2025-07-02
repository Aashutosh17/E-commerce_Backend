from http.client import HTTPException

from fastapi import APIRouter
from app.models.user_model import UserCreate
from app.database.connection import db
from app.core.jwt import create_access_token
from app.core.security import hash_password
import bcrypt
router = APIRouter()

@router.post("/signup")
async def signup(user:UserCreate):
    user_dict = user.model_dump()
    user_dict["password"] = hash_password(user_dict["password"])
    await db["users"].insert_one(user_dict)

    return {"message" : "User Created Successfully!"}


@router.post("/login")
async def signin(user:UserCreate):
    existing_user = await db["users"].find_one({"email": user.email})

    if not existing_user:
        raise HTTPException(status_code= 404, detail= "User not found!")

    if not bcrypt.checkpw(user.password.encode('utf-8'), existing_user["password"].encode('utf-8')):
        raise HTTPException(status_code = 401, detail = "Wrong Password")

    token = create_access_token({"email": user.email})
    return {"access_token": token, "token_type": "bearer"}

