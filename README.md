# AI Weather Wise API

## Project Description

AI Weather Wise API is a Flask-based weather application that provides current weather information for a selected city using the OpenWeather API.

## Features

- Get weather information by city name
- Current temperature
- Feels-like temperature
- Humidity
- Weather description
- JSON API response
- Flask REST API
- OpenWeather API integration

## Technologies Used

- Python
- Flask
- Requests
- OpenWeather API

## API Endpoint

GET:

/weather?city=Chennai

Example:

http://127.0.0.1:5000/weather?city=Chennai

## Sample Response

{
    "city": "Chennai",
    "temperature": 30,
    "feels_like": 33,
    "humidity": 70,
    "weather": "clear sky"
}

## How to Run

1. Install Python.
2. Install required packages:

   pip install -r requirements.txt

3. Configure the OpenWeather API key using the environment variable:

   OPENWEATHER_API_KEY

4. Run the application:

   python app.py

5. Open the API in a browser:

   http://127.0.0.1:5000

## Project Status

Completed and tested successfully.