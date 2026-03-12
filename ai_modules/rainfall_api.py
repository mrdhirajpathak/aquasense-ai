import requests
from config import WEATHER_API_KEY

def get_rainfall(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    rainfall = data.get("rain", {}).get("1h", 0)

    return rainfall
