# Write in google sheet function
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

# Write in google sheet
def write_in_google_sheet(tab_merged, spreadsheet_url, worksheet_name="Sites"):
    # Autorisations
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\...your google credential json file location...\\my-project-81259-122-0d35baf740ef.json", scope)
    client = gspread.authorize(creds)

    # Accès au Google Sheet
    spreadsheet = client.open_by_url(spreadsheet_url)

    # Création ou accès à la feuille
    try:
        worksheet = spreadsheet.worksheet(worksheet_name)
        worksheet.clear()
    except gspread.exceptions.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="100", cols="20")

    # Écriture du DataFrame dans la feuille
    set_with_dataframe(worksheet, tab_merged)
    msg = f"✅ Données écrites avec succès dans l'onglet '{worksheet_name}'."
    return msg
