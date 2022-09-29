from config import Config
import update_canceled_trips as update_canceled_trips
import utils.gtfs_rt_helper as gtfs_rt_helper
import threading
import time
from schedule import every, repeat, run_pending
# import schedule

# UPDATE_INTERVAL = 5

# def run_continuously(interval=UPDATE_INTERVAL):
#     cease_continuous_run = threading.Event()
#     class ScheduleThread(threading.Thread):
#         @classmethod
#         def run(cls):
#             while not cease_continuous_run.is_set():
#                 schedule.run_pending()
#                 time.sleep(interval)
#     continuous_thread = ScheduleThread()
#     continuous_thread.start()
#     return cease_continuous_run

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

def initial_load():
    update_canceled_trips.run_update()
    # gtfs_rt_helper.update_gtfs_realtime_data()
        
if __name__ == '__main__':

    while True:
        run_pending()
    # schedule.every().second.do(background_job('canceled_trips'))
    # schedule.every().second.do(test1)
    # schedule.every().second.do(test1)
    # schedule.every().second.do(background_job)
    # # background_job('canceled_trips')
    # # background_job('gtfs_rt')
    # stop_run_continuously = run_continuously()
    # schedule.every().second.do(background_job)
    # update_canceled_trips.run_update()
    