from config import Config
import update_canceled_trips as update_canceled_trips

import threading
import time
import schedule

UPDATE_INTERVAL = 30

def run_continuously(interval=UPDATE_INTERVAL):
    cease_continuous_run = threading.Event()
    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)
    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def background_job():
    update_canceled_trips.run_update()


if __name__ == '__main__':
    schedule.every().second.do(background_job)
    stop_run_continuously = run_continuously()
    # update_canceled_trips.run_update()
    