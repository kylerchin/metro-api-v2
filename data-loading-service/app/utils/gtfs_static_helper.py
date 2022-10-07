import pandas as pd
import json
from pathlib import Path
from sqlalchemy import create_engine
# from sqlalchemy.orm import Session,sessionmaker
from config import Config
from .database_connector import *
# from .utils.log_helper import *
# engine = create_engine(Config.DB_URI, echo=False,executemany_mode="values")
# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
CALENDAR_DATES_URL = 'https://gitlab.com/LACMTA/gtfs_bus/-/raw/weekly-updated-service/calendar_dates.txt'
# session = Session()

def update_calendar_dates():
    calendar_dates_df = pd.read_csv(CALENDAR_DATES_URL)
    calendar_dates_df.to_sql('calendar_dates',engine,index=False,if_exists="replace",schema=Config.TARGET_DB_SCHEMA)