def get_readable_status(status):
    if status == 0:
        return 'INCOMING_AT'
    if status == 1:
        return 'STOPPED_AT'
    if status == 2:
        return 'IN_TRANSIT_TO'