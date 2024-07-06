# Weather APIs Integration with Django

## Overview

This repository demonstrates how to integrate weather APIs using Django, fetching current weather data for different locations.

## Features

- Integration with OpenWeatherMap API.
- Display of current weather information for specified locations.

## Technologies Used

- Python
- Django
- Requests library

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/weather-api-django.git
    cd weather-api-django
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up API key:**

    - Obtain an API key from OpenWeatherMap.
    - Create a `.env` file in the project root and add your API key:

      ```env
      API_KEY_OPENWEATHERMAP=<your_openweathermap_api_key>
      ```

5. **Apply database migrations (if any):**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application in your browser at `http://localhost:8000`.
- Enter a location in the input field and click "Get Weather" to fetch current weather information using the OpenWeatherMap API.

## Project Structure

- `weatherapp/`: Django application directory.
  - `settings.py`: Django settings.
  - `urls.py`: URL routing.
  - `views.py`: Views for handling weather data retrieval.
  - `templates/`: HTML templates for rendering weather data.
