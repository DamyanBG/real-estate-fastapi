from fastapi import APIRouter

from db import db
from models.user_model import User

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/users", response_model=User)
async def create_user(user: User):
    user_ref = db.collection("Users").document()
    user_data = user.model_dump(by_alias=True, exclude_unset=True)
    user_ref.set(user_data)
    user_data["id"] = user_ref.id
    return user_data