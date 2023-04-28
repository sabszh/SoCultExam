import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json',scope)
client = gspread.authorize(credentials)

# sheet = client.create("SoCultSurvey")

# sheet.share('szhsabrina@gmail.com',perm_type = 'user', role='writer')

sheet = client.open("SoCultSurvey").sheet1

df = pd.read_csv("survey_df.csv")

sheet.update([df.columns.values.tolist()] + df.values.tolist())
