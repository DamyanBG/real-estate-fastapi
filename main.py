from fastapi import FastAPI
from google.cloud import firestore
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

from models.user_model import User

load_dotenv()

credentials = service_account.Credentials.from_service_account_file(
    os.environ["FIREBASE_CONFIG_PATH"]
)

# cred = credentials.Certificate(os.environ['FIREBASE_CONFIG_PATH'])
# initialize_app(cred)

db = firestore.Client(credentials=credentials, database="damyansfirestore2024")
app = FastAPI()


@app.post("/users", response_model=User)
async def create_user(user: User):
    user_ref = db.collection("Users").document()
    user_data = user.model_dump(by_alias=True, exclude_unset=True)
    user_ref.set(user_data)
    user_data["id"] = user_ref.id
    return user_data
