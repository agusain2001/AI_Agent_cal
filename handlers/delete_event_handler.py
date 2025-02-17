

from services.openai_service import get_function_call
from services.google_calendar_service import delete_event

def handle_delete_event(event_id):
    """
    Handles the logic to delete an event.
    Uses OpenAI to process the event deletion through function calling.
    """
    prompt = f"Delete the event with ID: {event_id}"
    
    function_call = get_function_call(prompt)
    
    if function_call and function_call.get("name") == "delete_event":
        # Call the Google Calendar service to delete the event
        delete_event(function_call["parameters"]["event_id"])
        return {"message": f"Event with ID {event_id} has been deleted."}
    else:
        return {"error": "Invalid function call response"}
