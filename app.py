from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")


@app.route("/")
def home():
    return jsonify({
        "message": "AI Weather Wise API is running!",
        "status": "success"
    })


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({
            "error": "Please provide a city name"
        }), 400

    if not API_KEY:
        return jsonify({
            "error": "OpenWeather API key is not configured"
        }), 500

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return jsonify({
            "error": "Unable to fetch weather data",
            "details": response.json()
        }), response.status_code

    data = response.json()

    return jsonify({
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    })


if __name__ == "__main__":
    app.run(debug=True)