from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: str = Field(None)
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    phone: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
