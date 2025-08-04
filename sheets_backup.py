# sheets_backup.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def append_to_sheet(row_data):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("sheets_key.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("Employee_Attendance_Backup").sheet1  # 🔁 your sheet name here
        sheet.append_row(list(row_data.values()))
        print(f"✅ Data appended successfully to Google Sheet: {row_data}")
        return True, f"Appended: {row_data}"

    except Exception as e:
        print(f"⚠️ Google Sheets backup failed: {e}")
        return False, str(e)
