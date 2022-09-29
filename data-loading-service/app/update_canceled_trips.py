from config import Config
from utils.ftp_helper import *
import os
import posixpath
from pathlib import Path

# from .utils.log_helper import *

PARENT_FOLDER = Path(__file__).parents[2]
TARGET_FILE = "CancelledTripsRT.json"
REMOTEPATH = '/nextbus/prod/'
# LOCALPATH = os.path.split(os.getcwd())[0]+'/appdata/'
TARGET_FOLDER = 'appdata'
TARGET_PATH = posixpath.join(PARENT_FOLDER,TARGET_FOLDER)
LOCALPATH = os.path.realpath(TARGET_PATH)
# ftp_json_file_time = ''

def run_update():
    try:
        # logger.info('pulling CancelledTripsRT.json from FTP')
        print('pulling CancelledTripsRT.json from FTP')
        if connect_to_ftp(REMOTEPATH, Config.SERVER, Config.USERNAME, Config.PASS):
            get_file_from_ftp(TARGET_FILE, LOCALPATH)
            # ftp_json_file_time = file_modified_time
            # Config.API_LAST_UPDATE_TIME = os.path.getmtime(LOCALPATH + TARGET_FILE)
        disconnect_from_ftp()
    except Exception as e:
        # logger.exception('FTP transfer failed: ' + str(e))
        print('FTP transfer failed: ' + str(e))
