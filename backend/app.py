from flask import Flask, request, jsonify
import pandas as pd
from joblib import load
from flask_cors import CORS

# Load the trained model (use raw string or double backslashes)
model = load(r"C:\PK\Data Analysis\Projects\Stroke Prediction\backend\stroke_prediction_model.joblib")
# Alternative: model = load("C:\\PK\\Data Analysis\\Projects\\Stroke Prediction\\backend\\stroke_prediction_model.joblib")

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (e.g., from React)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Convert to DataFrame (assuming data matches model input features)
        df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(df)[0]
        print(f"Prediction: {prediction}")

        # Return prediction as JSON
        return jsonify({"stroke": int(prediction)}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Welcome to the Stroke Prediction API"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)