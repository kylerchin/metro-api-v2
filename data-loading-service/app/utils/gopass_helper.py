
import pandas as pd
from .database_connector import *
from config import Config

def update_go_pass_data():
    try:
        GOOGLE_SHEET_MASTER_LIST_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSWbwrsqF-c---4lfw0LZWymd-f8sy8sLYkXgzh0OyeGATWwrvv7V1Mq5BcApn7F_-WYKP1KXy5shKw/pub?gid=893927551&single=true&output=csv'
        master_list_schools_df = pd.read_csv(GOOGLE_SHEET_MASTER_LIST_URL,usecols={'id','phone','participating','school','district','address','notes','resolved'})
        master_list_schools_df.to_sql('go_pass_schools',engine,index=False,if_exists="replace",schema=Config.TARGET_DB_SCHEMA)
    except Exception as e:
        print('Error updating Go Pass data: ' + str(e))