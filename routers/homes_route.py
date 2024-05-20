from fastapi import APIRouter, HTTPException

from db import db
from models.home_model import Home, HomeCreate, HomeUpdate

homes_router = APIRouter(prefix="/homes", tags=["homes"])

homes_ref = db.collection("homes")


@homes_router.post("/homes/", response_model=Home)
async def create_home(home: HomeCreate):
    """Create a new home listing."""
    data = home.model_dump()
    new_home_ref = homes_ref.document()  # Get a new document reference
    new_home_ref.set(data)
    data["id"] = new_home_ref.id  # Include the generated ID in the response
    return Home(**data)


@homes_router.put("/{home_id}", response_model=Home)
async def update_home(home_id: int, home: HomeUpdate):
    """Update an existing home listing."""
    home_ref = homes_ref.document(str(home_id))  # Firestore IDs are strings
    if not home_ref.get().exists:
        raise HTTPException(status_code=404, detail="Home not found")
    home_ref.update(home.model_dump())
    updated_home = home_ref.get()
    return Home(**updated_home.to_dict())


@homes_router.get("/", response_model=list[Home])
async def get_homes():
    """Get all home listings."""
    homes = []
    for doc in homes_ref.stream():
        home_data = doc.to_dict()
        home_data["id"] = doc.id
        homes.append(Home(**home_data))
    return homes


@homes_router.get("/{home_id}", response_model=Home)
async def get_home(home_id: int):
    """Get a specific home listing by ID."""
    home_ref = homes_ref.document(str(home_id))
    if not home_ref.get().exists:
        raise HTTPException(status_code=404, detail="Home not found")
    home_data = home_ref.get().to_dict()
    home_data["id"] = home_id
    return Home(**home_data)