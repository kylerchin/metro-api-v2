from config import Config
import update_canceled_trips as update_canceled_trips
import utils.gtfs_rt_helper as gtfs_rt_helper
import utils.gtfs_static_helper as gtfs_static_helper
import threading
import time
from schedule import every, repeat, run_pending
import pandas as pd

# import schedule

@repeat(every(60).seconds)
def gtfs_rt_scheduler():
    try:
        gtfs_rt_helper.update_gtfs_realtime_data()
    except Exception as e:
        print('Error updating GTFS-RT data: ' + str(e))

@repeat(every(15).minutes)
def canceled_trips_update_scheduler():
    try:
        update_canceled_trips.run_update()
    except Exception as e:
        print('Error updating canceled trips: ' + str(e))

@repeat(every(15).days)
def calendar_dates_update_scheduler():
    try:
        gtfs_static_helper.update_calendar_dates()
    except Exception as e:
        print('Error updating canceled trips: ' + str(e))

def initial_load():
    update_canceled_trips.run_update()
    gtfs_rt_helper.update_gtfs_realtime_data()
    gtfs_static_helper.update_calendar_dates()
        
if __name__ == '__main__':
    initial_load()
    if (Config.RUNNING_ENV == "prod") or (Config.RUNNING_ENV.contains("local")):
        while True:
            run_pending()
    