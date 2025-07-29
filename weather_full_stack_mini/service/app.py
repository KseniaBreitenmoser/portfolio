from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("../model/weather_classifier.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        temp_min = float(data['temp_min'])
        temp_max = float(data['temp_max'])
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400


    # Create a DataFrame with the same feature names as used during training
    features = pd.DataFrame([[temp_min, temp_max]], columns=['temp_min', 'temp_max'])

    # Predict class
    prediction = model.predict(features)[0]

    return jsonify({
            "Prediction": prediction,
            "input": {
                "temp_min": temp_min,
                "temp_max": temp_max
            }
    })

if __name__ == "__main__":
    app.run(debug=True)