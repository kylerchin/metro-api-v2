import os


def set_interval_time():
    try:
        current_environment = os.environ.get('RUNNING_ENV')
        if current_environment == 'prod':
            return 5
        else:
            return 120
    except Exception as e:
        print('Error setting db schema: ' + str(e))
        print('Defaulting to 200 seconds')
        return 200
