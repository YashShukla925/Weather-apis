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

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to your forked repository (`git push origin feature/new-feature`).
5. Submit a pull request on the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
