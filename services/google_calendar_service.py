

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config.settings import GOOGLE_CREDENTIALS_FILE, SCOPES

def get_calendar_service():
    """
    Initializes the Google Calendar API service.
    """
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_CREDENTIALS_FILE, scopes=SCOPES
    )
    service = build('calendar', 'v3', credentials=credentials)
    return service

def create_event(event_details):
    """
    Creates a new event on Google Calendar.
    """
    service = get_calendar_service()
    event = {
        'summary': event_details['summary'],
        'start': {'dateTime': event_details['start_time'], 'timeZone': 'UTC'},
        'end': {'dateTime': event_details['end_time'], 'timeZone': 'UTC'},
        'description': event_details.get('description', ''),
        'location': event_details.get('location', ''),
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event

def get_event(event_id):
    """
    Retrieves an event by ID from Google Calendar.
    """
    service = get_calendar_service()
    event = service.events().get(calendarId='primary', eventId=event_id).execute()
    return event

def update_event(event_id, updated_details):
    """
    Updates an existing event by ID in Google Calendar.
    """
    service = get_calendar_service()
    event = service.events().get(calendarId='primary', eventId=event_id).execute()
    event.update({
        'summary': updated_details.get('summary', event['summary']),
        'start': {'dateTime': updated_details.get('start_time', event['start']['dateTime']), 'timeZone': 'UTC'},
        'end': {'dateTime': updated_details.get('end_time', event['end']['dateTime']), 'timeZone': 'UTC'},
        'description': updated_details.get('description', event.get('description', '')),
        'location': updated_details.get('location', event.get('location', '')),
    })
    updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()
    return updated_event

def delete_event(event_id):
    """
    Deletes an event by ID from Google Calendar.
    """
    service = get_calendar_service()
    service.events().delete(calendarId='primary', eventId=event_id).execute()
