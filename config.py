from dotenv import load_dotenv
import os

load_dotenv()

FIREBASE_CONFIG_PATH = os.environ["FIREBASE_CONFIG_PATH"]
BUCKET_NAME = os.environ["BUCKET_NAME"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
