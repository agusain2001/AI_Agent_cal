

from services.openai_service import get_function_call
from services.google_calendar_service import create_event

def handle_create_event(event_details):
    """
    Handles the logic to create a new event.
    Uses OpenAI to process the event creation through function calling.
    """
    prompt = f"Create an event with the following details: {event_details}"
    
    function_call = get_function_call(prompt)
    
    if function_call and function_call.get("name") == "create_event":
        # Call the Google Calendar service to create the event
        event_details = function_call["parameters"]
        event = create_event(event_details)
        return event
    else:
        return {"error": "Invalid function call response"}
