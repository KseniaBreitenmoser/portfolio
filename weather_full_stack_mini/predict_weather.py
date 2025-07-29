import requests
import sys

# check if the correct number of the arguments is provided
if len(sys.argv) != 3:
    print("Incorrect number of arguments provided")
    sys.exit(1)

try:
    temp_min = float(sys.argv[1])
    temp_max = float(sys.argv[2])
except ValueError:
    print("Error: Both arguments must be numbers (floats or integers)")
    sys.exit(1)

url = "http://127.0.0.1:5000/predict"
payload = {
    "temp_min": temp_min,
    "temp_max": temp_max
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    result = response.json()
    print("Prediction result:")
    print(f" Input -> temp_min: {temp_min}, temp_max: {temp_max}")
    print(f" Prediction -> {result['Prediction']}")
else:
    print("Error: ", response.status_code, response.text)
    
