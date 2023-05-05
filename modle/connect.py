import os
import google.auth
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

class GoogleSheet:
    def __init__(self, spreadsheet_id, api_key=None):
        self.spreadsheet_id = spreadsheet_id
        self.api_key = api_key

        # authenticate your application
        if self.api_key is not None:
            self.service = build('sheets', 'v4', developerKey=self.api_key)
        else:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'
            creds, project = google.auth.default(scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets'])
            self.service = build('sheets', 'v4', credentials=creds)

    def get_values(self, range_name):
        # call the Sheets API to retrieve the data
        result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=range_name).execute()

        # return the retrieved data
        rows = result.get('values', [])
        return rows