from flask import Flask, render_template, request

app = Flask(__name__)

# Expanded weather data with more cities
weather_data = {
    "Delhi": {"temperature": "30°C", "description": "Sunny"},
    "Mumbai": {"temperature": "28°C", "description": "Humid"},
    "Chennai": {"temperature": "35°C", "description": "Hot"},
    "Kolkata": {"temperature": "33°C", "description": "Cloudy"},
    "Bangalore": {"temperature": "25°C", "description": "Pleasant"},
    "Hyderabad": {"temperature": "32°C", "description": "Sunny"},
    "Pune": {"temperature": "27°C", "description": "Pleasant"},
    "Ahmedabad": {"temperature": "38°C", "description": "Very Hot"},
    "Jaipur": {"temperature": "36°C", "description": "Hot"},
    "Lucknow": {"temperature": "34°C", "description": "Humid"},
    "Chandigarh": {"temperature": "29°C", "description": "Mild"},
    "Patna": {"temperature": "31°C", "description": "Sunny"},
    "Indore": {"temperature": "28°C", "description": "Warm"},
    "Nagpur": {"temperature": "40°C", "description": "Scorching"},
    "Bhopal": {"temperature": "30°C", "description": "Warm"},
    "Vadodara": {"temperature": "33°C", "description": "Hot"},
    "Thiruvananthapuram": {"temperature": "31°C", "description": "Humid"},
    "Surat": {"temperature": "32°C", "description": "Humid"},
    "Coimbatore": {"temperature": "26°C", "description": "Pleasant"},
    "Mysore": {"temperature": "24°C", "description": "Cool"},
    "Kanpur": {"temperature": "37°C", "description": "Hot"},
    "Raipur": {"temperature": "34°C", "description": "Sunny"},
    "Varanasi": {"temperature": "33°C", "description": "Cloudy"},
    "Agra": {"temperature": "35°C", "description": "Hot"},
    "Dehradun": {"temperature": "22°C", "description": "Cool"},
    "Shimla": {"temperature": "18°C", "description": "Chilly"},
    "Manali": {"temperature": "15°C", "description": "Snowy"},
    "Goa": {"temperature": "30°C", "description": "Tropical"},
    "Guwahati": {"temperature": "29°C", "description": "Humid"},
    "Darjeeling": {"temperature": "17°C", "description": "Foggy"},
    "Pondicherry": {"temperature": "31°C", "description": "Breezy"},
    "Ranchi": {"temperature": "28°C", "description": "Pleasant"},
    "Jodhpur": {"temperature": "39°C", "description": "Hot"},
    "Udaipur": {"temperature": "37°C", "description": "Sunny"},
    "Amritsar": {"temperature": "33°C", "description": "Sunny"},
    "Ajmer": {"temperature": "35°C", "description": "Dry"},
    "Shillong": {"temperature": "21°C", "description": "Misty"},
    "Itanagar": {"temperature": "23°C", "description": "Pleasant"},
    "Aizawl": {"temperature": "25°C", "description": "Cloudy"},
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    city_weather = weather_data.get(city.capitalize())

    if city_weather:
        return render_template(
            "result.html",
            city=city,
            temperature=city_weather["temperature"],
            description=city_weather["description"],
        )
    else:
        error_message = f"Sorry, we don't have data for {city}."
        return render_template("index.html", error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
