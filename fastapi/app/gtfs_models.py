# gtfsrdb.py: load gtfs-realtime data to a database

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Float, MetaData
from sqlalchemy.orm import relationship, backref

GTFSrtBase = declarative_base(metadata=MetaData(schema="metro_api_dev"))

# classes for the GTFS-realtime data
# TripUpdate
# StopTimeUpdate
# VehiclePosition

class TripUpdate(GTFSrtBase):
    __tablename__ = 'trip_updates'
    oid = Column(Integer, primary_key=True)

    # This replaces the TripDescriptor message
    # TODO: figure out the relations
    trip_id = Column(String(64))
    route_id = Column(String(64))
    start_time = Column(String(8))
    start_date = Column(String(10))
    # Put in the string value not the enum
    # TODO: add a domain
    schedule_relationship = Column(String(9))
    direction_id = Column(Integer)
    
    # moved from the header, and reformatted as datetime
    timestamp = Column(Integer)
    # StopTimeUpdates = relationship('StopTimeUpdate', backref='TripUpdate')
    class Config:
        schema_extra = {
            "definition": {
                "comment": 
                """
                # Metro's bus agency id is "LACMTA"
                # Metro's rail agency id is "LACMTA METRO
                """
            }
        }

class StopTimeUpdate(GTFSrtBase):
    __tablename__ = 'stop_time_updates'
    # oid = Column(Integer, )

    # TODO: Fill one from the other
    stop_sequence = Column(Integer)
    stop_id = Column(String(10),primary_key=True)

    # TODO: Add domain
    schedule_relationship = Column(String(9))
    # Link it to the TripUpdate
    # trip_update_id = Column(Integer, ForeignKey('trip_updates.oid'))

class VehiclePosition(GTFSrtBase):
    __tablename__ = "vehicle_position_updates"

    # Vehicle information
    current_stop_sequence = Column(Integer)
    current_status = Column(String)
    timestamp = Column(Integer)
    stop_id = Column(String)

    # Collapsed Vehicle.trip
    trip_id = Column(String)
    trip_start_date = Column(String)
    trip_route_id = Column(String)

    # Collapsed Vehicle.Position
    position_latitude = Column(Float)
    position_longitude = Column(Float)
    position_bearing = Column(Float)
    position_speed = Column(Float)

    # collapsed Vehicle.Vehicle
    vehicle_id = Column(String,primary_key=True)
    vehicle_label = Column(String)

    timestamp = Column(Integer)


# So one can loop over all classes to clear them for a new load (-o option)
AllClasses = (TripUpdate, StopTimeUpdate, VehiclePosition)