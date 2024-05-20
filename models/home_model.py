from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal


class HomeBase(BaseModel):  # For common fields used in creation/update
    title: str = Field(..., max_length=100)
    city: str
    neighborhood: str = Field(..., max_length=50)  # Adjust length limits if needed
    address: str
    price: Decimal
    bathrooms: int
    garages: int
    bedrooms: int
    area: Decimal
    year: int = Field(..., ge=1800, le=2024)  # Constrain year to reasonable values
    description: str = Field(..., max_length=1000)
    longitude: Decimal
    latitude: Decimal
    owner_id: int


class HomeCreate(HomeBase):
    pass  # Use this for creating new homes (no ID yet)


class HomeUpdate(HomeBase):
    pass  # For updating, same fields, but IDs might be present


class Home(HomeBase):
    id: int
    owner: Optional[str] = None  # Might come from a joined query
    home_views: int = 0

    class Config:
        from_attributes = True  # For easy conversion from your ORM objects
