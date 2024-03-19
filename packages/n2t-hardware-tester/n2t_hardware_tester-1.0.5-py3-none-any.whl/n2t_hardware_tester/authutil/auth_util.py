import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from n2t_hardware_tester.n2tconfig import GOOGLE_API_CREDENTIALS, GOOGLE_API_TOKENS_PATH


def auth_on_google_classroom():
    credentials_path = GOOGLE_API_CREDENTIALS
    tokens_path = GOOGLE_API_TOKENS_PATH
    SCOPES = [
        "https://www.googleapis.com/auth/classroom.courses.readonly",
        "https://www.googleapis.com/auth/classroom.coursework.students",
        "https://www.googleapis.com/auth/classroom.rosters",
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/spreadsheets",
    ]
    creds = None
    if os.path.exists(tokens_path):
        creds = Credentials.from_authorized_user_file(tokens_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(tokens_path, "w") as token:
            token.write(creds.to_json())
    return creds
