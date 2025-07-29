import requests
from datetime import datetime
from fetch_weather import fetch_weather

# 1. Fetch latest weather forecast
df = fetch_weather()
today_row = df.iloc[0] # only takes the first day of 7

temp_min = today_row['temp_min']
temp_max = today_row['temp_max']
date = today_row['date']

# 2. Call prediction API
url = "http://127.0.0.1:5000/predict"
payload = {
    "temp_min": temp_min,
    "temp_max": temp_max
}

response = requests.post(url, json=payload)

# 3. Log results
if response.status_code == 200:
    result = response.json()
    prediction = result['Prediction']
    with open("daily_predictions.log", "a") as f:
        log_line = f"{datetime.now().isoformat()} | Date: {date} | Min: {temp_min} | Max: {temp_max} | Prediction: {prediction}\n"
        f.write(log_line)

    print("Prediction logged:")
    print(log_line)
else:
    print("Error calling API:", response.status_code, response.txt)