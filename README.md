# Google Calendar Event Management with OpenAI

## Project Description

This project is a Flask-based API that integrates OpenAI's function calling with Google Calendar. The application provides endpoints to create, read, update, and delete calendar events. It uses OpenAI's language model to process event-related requests and validate actions before interacting with Google Calendar through the API.

## Prerequisites

Before running the project, ensure you have the following installed and set up:

- Python 3.8+
- Flask
- Google Cloud Project with Google Calendar API enabled
- OpenAI API key
- Google service account credentials for accessing the Calendar API

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/agusain2001/AI_Agent_cal.git
   ```
2. Navigate to the project directory:
   ```bash
   cd google-calendar-openai
   ```
3. Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

##Configuration

The application uses the following configuration files:

- **config/settings.py**: Contains the Google Calendar API credentials and OpenAI API key.

- **config.py**: Configuration for the Flask app and any additional settings.

## Usage
   
 1. To start the Flask application, run the following command in the terminal:
   ```bash
      python app.py
   ```
 2. The following API endpoints are available:

   - **POST /create_event**: Create a new event in the calendar.

   - **GET /get_event**: Retrieve event details using event ID.

   - **PUT /update_event**: Update an existing event using event ID.

   - **DELETE /delete_event**: Delete an event using event ID.

## API Example Usage
   Examples of API requests to interact with the Google Calendar through OpenAI function calling:

1. **POST /create_event**: Example request body
      ```bash
      {
       "summary": "Team Meeting",
       "start_time": "2025-02-25T09:00:00",
       "end_time": "2025-02-25T10:00:00",
       "description": "Discuss project updates",
       "location": "Conference Room 1"
      }
      ```
 2. **GET /get_event**: Example request
    ```bash
      GET /get_event?event_id=event_id_here
    ```
3. **PUT /update_event**: Example request body
   ```bash
   {
       "event_id": "event_id_here",
       "summary": "Updated Team Meeting",
       "start_time": "2025-02-25T10:00:00",
       "end_time": "2025-02-25T11:00:00",
       "description": "Discuss project updates and planning"
   }
   ```
4. **DELETE /delete_event**: Example request body
   ```bash
   {
       "event_id": "event_id_here"
   }
   ```









