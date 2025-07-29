import requests
import pandas as pd
from datetime import date

def fetch_weather(latitude=47.05, longitude=8.31):
    today = date.today().isoformat()

    url = "https://api.open-meteo.com/v1/forecast"

    payload = {
    "latitude": 47.05,
    "longitude": 8.31,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "past_days": 60,
    "timezone": "auto"
    }

    response = requests.get(url,params=payload)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame({
        "date": data['daily']['time'],
        "temp_max": data['daily']['temperature_2m_max'],
        "temp_min": data['daily']['temperature_2m_min']
    })

    return df

if __name__ == "__main__":
    df = fetch_weather()
    print(df)