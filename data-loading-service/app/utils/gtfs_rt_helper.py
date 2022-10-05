try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
from cgi import print_arguments
import datetime
from multiprocessing.resource_sharer import stop

# from ..gtfs_rt import *
# from ..models import *

import json
import requests
import pandas as pd

import timeit
from datetime import datetime
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import create_engine, inspect
from models.gtfs_rt import *
from config import Config

from utils.gtfs_realtime_pb2 import FeedMessage
from .database_connector import Session,get_db

# from ..schemas import TripUpdates, StopTimeUpdates,VehiclePositions
from datetime import datetime


API_URL = 'https://api.metro.net/'
VEHICLE_POSITIONS_ENDPOINT = API_URL + 'vehicle_positions/bus?output_format=json'
TRIP_UPDATES_ENDPOINT = API_URL + 'trip_updates/bus'
STOP_TIMES_ENDPOINT = API_URL + 'bus/stop_times/'
STOPS_ENDPOINT = API_URL + 'bus/stops/'


SWIFTLY_API_REALTIME = 'https://api.goswift.ly/real-time/'
SWIFTLY_GTFS_RT_TRIP_UPDATES = 'gtfs-rt-trip-updates'
SWIFTLY_GTFS_RT_VEHICLE_POSITIONS = 'gtfs-rt-vehicle-positions'

engine = create_engine(Config.DB_URI, echo=False,executemany_mode="values")

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

insp = inspect(engine)
session = Session()

SERVICE_DICT = {
    'bus': 'lametro',
    'rail': 'lametro-rail'
}

# Connect to the database
def connect_to_db():
    try:
        print('Connecting to the database')
        db = Session()
        yield db
    except Exception as e:
        print(e)
        raise e
    finally:
        session.close()

def connect_to_swiftly(service, endpoint):
    swiftly_endpoint = ''

    swiftly_endpoint = SWIFTLY_API_REALTIME + SERVICE_DICT[service] + '/' + endpoint

    if (service == 'bus'):
        key = Config.SWIFTLY_AUTH_KEY_BUS
    elif (service == 'rail'):
        key = Config.SWIFTLY_AUTH_KEY_RAIL
    header = { 
        "Authorization": key
    }
    try:
        print('Connecting to Swiftly API: ' + swiftly_endpoint)
        response = requests.get(swiftly_endpoint, headers=header)
        print('Response status code: ' + str(response.status_code))
        return response.content
    except Exception as e:
        print.exception('Error connecting to Swiftly API: ' + str(e))
        return

def update_gtfs_realtime_data():
    process_start = timeit.default_timer()
    connect_to_db()

    feed = FeedMessage()
    response_data = connect_to_swiftly('bus', SWIFTLY_GTFS_RT_TRIP_UPDATES)
    feed.ParseFromString(response_data)
    
    trip_update_array = []
    stop_time_array = []
    vehicle_position_update_array = []
    for entity in feed.entity:
        trip_update_array.append({
            'trip_id': entity.trip_update.trip.trip_id,
            'route_id': entity.trip_update.trip.route_id,
            'start_time': entity.trip_update.trip.start_time,
            'start_date': entity.trip_update.trip.start_date,
            'direction_id': entity.trip_update.trip.direction_id,
            'schedule_relationship': entity.trip_update.trip.schedule_relationship,
            'timestamp': entity.trip_update.timestamp
        })
        for stop_time_update in entity.trip_update.stop_time_update:
            stop_time_array.append({
                'trip_id': entity.trip_update.trip.trip_id,
                'stop_id': stop_time_update.stop_id,
                'arrival': stop_time_update.arrival.time,
                'departure': stop_time_update.departure.time,
                'schedule_relationship': stop_time_update.schedule_relationship
            })

    trip_update_df = pd.DataFrame(trip_update_array)
    stop_time_df = pd.DataFrame(stop_time_array)
    # print(trip_update_df)
    # print(stop_time_df)
    vehicle_positions_feed = FeedMessage()
    response_data = connect_to_swiftly('bus', SWIFTLY_GTFS_RT_VEHICLE_POSITIONS)
    vehicle_positions_feed.ParseFromString(response_data)
    # print(vehicle_positions_feed)
    for entity in vehicle_positions_feed.entity:
        if entity.HasField('vehicle'):
            vehicle_position_update_array.append({
                'current_stop_sequence': entity.vehicle.current_stop_sequence,
                'current_status': entity.vehicle.current_status,
                'timestamp': entity.vehicle.timestamp,
                'stop_id': entity.vehicle.stop_id,
                'trip_id': entity.vehicle.trip.trip_id,
                'trip_start_date': entity.vehicle.trip.start_date,
                'trip_route_id': entity.vehicle.trip.route_id,
                'position_latitude': entity.vehicle.position.latitude,
                'position_longitude': entity.vehicle.position.longitude,
                'position_bearing': entity.vehicle.position.bearing,
                'position_speed': entity.vehicle.position.speed,
                'vehicle_id': entity.vehicle.vehicle.id,
                'vehicle_label': entity.vehicle.vehicle.label
            })
    vehicle_position_updates = pd.DataFrame(vehicle_position_update_array)
    # logging('vehicle_position_updates Data Frame: ' + str(vehicle_position_updates))
    vehicle_position_updates.to_sql('vehicle_position_updates',engine,index=False,if_exists="replace",schema=Config.TARGET_DB_SCHEMA)
    stop_time_df.to_sql('stop_time_updates',engine,index=False,if_exists="replace",schema=Config.TARGET_DB_SCHEMA)
    trip_update_df.to_sql('trip_updates',engine,index=False,if_exists="replace",schema=Config.TARGET_DB_SCHEMA)
    process_end = timeit.default_timer()
    # print('===GTFS Update process took {} seconds'.format(process_end - process_start)+"===")
    print('===GTFS Update process took {} seconds'.format(process_end - process_start)+"===")
    
if __name__ == "__main__":
    process_start = timeit.default_timer()
    # update_gtfs_realtime_data()
    process_end = timeit.default_timer()
    session.close()
    print('Process took {} seconds'.format(process_end - process_start))