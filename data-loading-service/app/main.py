from config import Config
import update_canceled_trips as update_canceled_trips
import utils.gtfs_rt_helper as gtfs_rt_helper
import utils.gtfs_static_helper as gtfs_static_helper
import utils.gopass_helper as gopass_helper
import utils.main_helper as main_helper
import threading
import time
from schedule import every, repeat, run_pending
import pandas as pd
# import schedule

@repeat(every(main_helper.set_interval_time()).seconds)
def gtfs_rt_scheduler():
    try:
        gtfs_rt_helper.update_gtfs_realtime_data()
    except Exception as e:
        print('Error updating GTFS-RT data: ' + str(e))

@repeat(every(1).day)
def go_pass_data_scheduler():
    try:
        gopass_helper.update_go_pass_data()
    except Exception as e:
        print('Error updating GTFS-RT data: ' + str(e))

@repeat(every(15).minutes)
def canceled_trips_update_scheduler():
    try:
        update_canceled_trips.run_update()
    except Exception as e:
        print('Error updating canceled trips: ' + str(e))

@repeat(every(7).days)
def calendar_dates_update_scheduler():
    try:
        gtfs_static_helper.update_calendar_dates()
        # gtfs_static_helper.update_gtfs_static_files()
    except Exception as e:
        print('Error updating canceled trips: ' + str(e))
        
def initial_load():
    update_canceled_trips.run_update()
    gtfs_rt_helper.update_gtfs_realtime_data()
    gtfs_static_helper.update_calendar_dates()
    # gtfs_static_helper.update_gtfs_static_files()
    gopass_helper.update_go_pass_data()
        
if __name__ == '__main__':
    initial_load()
    while True:
        run_pending()