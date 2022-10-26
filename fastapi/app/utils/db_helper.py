def vehicle_position_reformat(row):
        trip_info = {}
        vehicle_info = {}
        position_info = {}

        if row.trip_id:
            trip_info['trip_id'] = row.trip_id
            del row.trip_id
        if row.trip_route_id:
            trip_info['route_id'] = row.trip_route_id
            del row.trip_route_id
        if row.trip_start_date:
            trip_info['trip_start_date'] = row.trip_start_date
            del row.trip_start_date      
        if row.vehicle_id:
            vehicle_info['vehicle_id'] = row.vehicle_id
            del row.vehicle_id
        if row.vehicle_label:
            vehicle_info['vehicle_label'] = row.vehicle_label
            del row.vehicle_label
        if row.position_latitude:
            position_info['latitude'] = row.position_latitude
            del row.position_latitude
        if row.position_longitude:
            position_info['longitude'] = row.position_longitude
            del row.position_longitude
        if row.position_bearing:
            position_info['bearing'] = row.position_bearing
            del row.position_bearing
        if row.position_speed:
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