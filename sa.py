from google.oauth2 import service_account

from config import FIREBASE_CONFIG_PATH


credentials = service_account.Credentials.from_service_account_file(
    FIREBASE_CONFIG_PATH
)
