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
   git clone https://github.com/your-repository/google-calendar-openai.git
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















