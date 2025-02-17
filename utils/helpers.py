

from datetime import datetime

def validate_event_details(event_details):
    """
    Validates the event details to ensure that required fields are provided
    and that start time is before end time.
    """
    required_fields = ['summary', 'start_time', 'end_time']
    
    for field in required_fields:
        if field not in event_details or not event_details[field]:
            return False
    
    try:
        # Check if the start and end times are valid datetime strings
        start_time = datetime.fromisoformat(event_details['start_time'])
        end_time = datetime.fromisoformat(event_details['end_time'])
        if start_time >= end_time:
            return False
    except ValueError:
        return False
    
    return True
