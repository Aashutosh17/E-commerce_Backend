from fastapi import APIRouter
from app.models.user_model import UserCreate
from app.database.connection import db
from app.core.security import hash_password

router = APIRouter()

@router.post("/signup")
async def signup(user:UserCreate):
    user_dict = user.model_dump()
    user_dict["password"] = hash_password(user_dict["password"])
    await db["users"].insert_one(user_dict)

    return {"message" : "User Created Successfully!"}
