from fastapi import APIRouter
from routers import user_route, homes_route, images_route

api_router = APIRouter()
api_router.include_router(user_route.user_router)
api_router.include_router(homes_route.homes_router)
api_router.include_router(images_route.images_router)
