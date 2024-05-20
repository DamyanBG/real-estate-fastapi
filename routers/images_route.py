from fastapi import APIRouter

from db import db
from storage.google_cloud_storage import upload_base64_image, generate_signed_url
from models.image_model import Image, ImageCreate, ImageResp

images_router = APIRouter(prefix="/images", tags=["images"])

images_ref = db.collection("Images")


@images_router.post("/", response_model=ImageResp)
async def create_home(image: ImageCreate):
    """Create a new home listing."""
    data = image.model_dump()
    base64_data = data["photo_base64"]
    img_file_name = upload_base64_image(base64_data)
    new_image_ref = images_ref.document()
    new_image_data = {"file_name": img_file_name}
    new_image_ref.set(new_image_data)
    new_image_data["id"] = new_image_ref.id
    new_image_url = generate_signed_url(img_file_name)
    new_image_data["url"] = new_image_url
    return ImageResp(**new_image_data)
