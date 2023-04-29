import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np


scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/gs_credentials.json',scope)
client = gspread.authorize(credentials)

#sheet_survey = client.create("SoCultExam_Survey_df")
#sheet_chathistory = client.create("SoCultExam_Chathistory_df")

#sheet_survey.share('szhsabrina@gmail.com',perm_type = 'user', role='writer')
#sheet_chathistory.share('szhsabrina@gmail.com',perm_type = 'user', role='writer')

sheet_survey = client.open("SoCultExam_Survey_df").sheet1
sheet_chathistory = client.open("SoCultExam_Chathistory_df").sheet1

df_survey = pd.read_csv("C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/survey_df.csv", delimiter=";", encoding='utf-8')
df_chathistory = pd.read_csv("C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/chathistory.csv", delimiter=";", encoding='utf-8')

# replace infinite and NaN values with 0
df_survey = df_survey.replace([np.inf, -np.inf, np.nan], 0)
df_chathistory = df_chathistory.replace([np.inf, -np.inf, np.nan], 0)

# Update the Google Sheets
sheet_survey.update([df_survey.columns.values.tolist()] + df_survey.values.tolist())
sheet_chathistory.update([df_chathistory.columns.values.tolist()] + df_chathistory.values.tolist())