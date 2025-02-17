

from services.openai_service import get_function_call
from services.google_calendar_service import get_event

def handle_get_event(event_id):
    """
    Handles the logic to retrieve an event's details.
    Uses OpenAI to process the event retrieval through function calling.
    """
    prompt = f"Retrieve the details of the event with ID: {event_id}"
    
    function_call = get_function_call(prompt)
    
    if function_call and function_call.get("name") == "get_event":
        # Call the Google Calendar service to get the event details
        event = get_event(function_call["parameters"]["event_id"])
        return event
    else:
        return {"error": "Invalid function call response"}
