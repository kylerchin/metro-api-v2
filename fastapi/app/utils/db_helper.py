import json
def trip_update_reformat(row):
    result_row = {}
    result_row['id'] = row.trip_id
    trip_update = {}    
    trip_update['timestamp'] = row.timestamp

    trip = {}
    if 'trip_id' in row:
        trip['tripid'] = row.trip_id
    if 'start_time' in row:
        trip['startTime'] = row.start_time
    if 'start_date' in row:
        trip['startDate'] = row.start_date
    if 'schedule_relationship' in row:
        trip['scheduleRelationship'] = get_readable_schedule_relationship(row.schedule_relationship)
    if 'route_id' in row:
        trip['routeId'] = row.route_id
    if 'direction_id' in row:
        trip['directionId'] = row.direction_id
    trip_update['trip'] = trip

    stop_time_updates = []
    
    if 'stop_time_json' in row:
        clean_stop_time_json = row.stop_time_json.replace("'", '"')
        for stop_time in json.loads(clean_stop_time_json):
            this_stop_time = {}
            if 'stop_squence' in stop_time:
                this_stop_time['stopSequence'] = stop_time['stop_sequence']
            if 'arrival' in stop_time:
                this_stop_time['arrival']['time'] = stop_time['arrival']
            if 'departure' in stop_time:
                this_stop_time['departure']['time'] = stop_time['departure']
            if 'schedule_relationship' in stop_time:
                this_stop_time['scheduleRelationship'] = get_readable_schedule_relationship(stop_time['schedule_relationship'])
            if 'stop_id' in stop_time:
                this_stop_time['stopId'] = stop_time['stop_id']
            stop_time_updates.append(this_stop_time)
    trip_update['stopTimeUpdates'] = stop_time_updates
    result_row['tripUpdate'] = trip_update
    return result_row


def vehicle_position_reformat(row):
        trip_info = {}
        vehicle_info = {}
        position_info = {}

        if 'trip_id' in row:
            trip_info['trip_id'] = row.trip_id
            del row.trip_id
        if 'trip_route_id' in row:
            trip_info['route_id'] = row.trip_route_id
            del row.trip_route_id
        if 'trip_start_date' in row:
            trip_info['trip_start_date'] = row.trip_start_date
            del row.trip_start_date      
        if 'vehicle_id' in row:
            vehicle_info['vehicle_id'] = row.vehicle_id
            del row.vehicle_id
        if 'vehicle_label' in row:
            vehicle_info['vehicle_label'] = row.vehicle_label
            del row.vehicle_label
        if 'position_latitude' in row:
            position_info['latitude'] = row.position_latitude
            del row.position_latitude
        if 'position_longitude' in row:
            position_info['longitude'] = row.position_longitude
            del row.position_longitude
        if 'position_bearing' in row:
            position_info['bearing'] = row.position_bearing
            del row.position_bearing
        if 'position_speed' in row:
            position_info['speed'] = row.position_speed
            del row.position_speed

        row.trip = trip_info
        row.vehicle = vehicle_info
        row.position = position_info
        row.current_status = get_readable_status(row.current_status)
        return row

def get_readable_status(status):
    if status == 0:
        return 'INCOMING_AT'
    if status == 1:
        return 'STOPPED_AT'
    if status == 2:
        return 'IN_TRANSIT_TO'

def get_readable_schedule_relationship(schedule_relationship):
    if schedule_relationship == 0:
        return 'SCHEDULED'
    if schedule_relationship == 1:
        return 'SKIPPED'
    if schedule_relationship == 2:
        return 'NO_DATA'
    if schedule_relationship == 3:
        return 'UNSCHEDULED'
