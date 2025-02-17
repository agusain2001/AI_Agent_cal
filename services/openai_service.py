

import openai
from config.settings import OPENAI_API_KEY

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_function_call(prompt):
    """
    Interacts with OpenAI API for function calling and returns the function call to be executed.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": prompt}],
        functions=[
            {
                "name": "create_event",
                "description": "Create a new event in the calendar",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Event title"},
                        "start_time": {"type": "string", "description": "Start time in ISO format"},
                        "end_time": {"type": "string", "description": "End time in ISO format"},
                        "description": {"type": "string", "description": "Event description"},
                        "location": {"type": "string", "description": "Event location"},
                    },
                    "required": ["summary", "start_time", "end_time"]
                },
            },
            {
                "name": "get_event",
                "description": "Retrieve details of an event",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {"type": "string", "description": "ID of the event to retrieve"},
                    },
                    "required": ["event_id"]
                },
            },
            {
                "name": "update_event",
                "description": "Update an existing event",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {"type": "string", "description": "ID of the event to update"},
                        "summary": {"type": "string", "description": "Updated event title"},
                        "start_time": {"type": "string", "description": "Updated start time in ISO format"},
                        "end_time": {"type": "string", "description": "Updated end time in ISO format"},
                        "description": {"type": "string", "description": "Updated event description"},
                        "location": {"type": "string", "description": "Updated event location"},
                    },
                    "required": ["event_id"]
                },
            },
            {
                "name": "delete_event",
                "description": "Delete an event",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {"type": "string", "description": "ID of the event to delete"},
                    },
                    "required": ["event_id"]
                },
            },
        ],
        function_call="auto",
    )
    return response.choices[0].message.get("function_call")
