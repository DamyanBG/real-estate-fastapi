from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.routes import api_router

origins = ["http://localhost", "http://localhost:5173"]

app = FastAPI()
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
