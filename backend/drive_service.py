from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
SERVICE_ACCOUNT_FILE = "service_account.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build("drive", "v3", credentials=credentials)

FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID")


def search_drive_files(query: str):
    response = service.files().list(
        q=f"'{FOLDER_ID}' in parents and {query}",
        fields="files(id,name,mimeType,webViewLink,modifiedTime)",
        pageSize=10
    ).execute()

    return response.get("files", [])