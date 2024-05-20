from fastapi import FastAPI, HTTPException, Depends

from routers.routes import api_router




app = FastAPI()
app.include_router(api_router)





