

from services.openai_service import get_function_call
from services.google_calendar_service import update_event

def handle_update_event(event_id, updated_details):
    """
    Handles the logic to update an existing event.
    Uses OpenAI to process the event update through function calling.
    """
    prompt = f"Update the event with ID: {event_id} with the following details: {updated_details}"
    
    function_call = get_function_call(prompt)
    
    if function_call and function_call.get("name") == "update_event":
        # Call the Google Calendar service to update the event
        updated_event = update_event(function_call["parameters"]["event_id"], function_call["parameters"])
        return updated_event
    else:
        return {"error": "Invalid function call response"}
