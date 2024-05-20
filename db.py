from google.cloud import firestore
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

load_dotenv()

credentials = service_account.Credentials.from_service_account_file(
    os.environ["FIREBASE_CONFIG_PATH"]
)

DATABASE_NAME = os.environ["FIREBASE_CONFIG_PATH"]

db = firestore.Client(credentials=credentials, database=DATABASE_NAME)
