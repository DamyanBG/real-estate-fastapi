from fastapi import APIRouter

from db import db
from utils.enums import RoleType
from models.user_model import User, UserCreate

user_router = APIRouter(prefix="/users", tags=["users"])

user_ref = db.collection("Users")


@user_router.post("/register-seller", response_model=User)
async def create_user(user: UserCreate):
    new_user_ref = user_ref.document()
    user_data = user.model_dump(by_alias=True, exclude_unset=True)
    user_data["role"] = RoleType.seller
    new_user_ref.set(user_data)
    user_data["id"] = new_user_ref.id
    return user_data
