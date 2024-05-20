from pydantic import Field, BaseModel


class Image(BaseModel):
    id: str = Field(..., description="Unique identifier for the image")
    file_name: str = Field(..., description="URL where the image is stored")


class ImageCreate(BaseModel):
    photo_base64: str = Field(...)


class ImageResp(BaseModel):
    url: str = Field(...)
