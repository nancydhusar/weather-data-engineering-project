import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITY = "Hannover"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

weather_data = {
    "city": CITY,
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "wind_speed": data["wind"]["speed"],
    "weather": data["weather"][0]["main"],
    "timestamp": datetime.now()
}

df = pd.DataFrame([weather_data])

file_path = "data/weather_data.csv"



if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=False, index=False)
else:
    df.to_csv(file_path, index=False)

print("Weather data saved successfully!")