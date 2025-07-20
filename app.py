from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "✅ CK AI BOT API is running! Use POST /predict or /predict_ai."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    numbers = data.get("numbers")

    if not numbers or len(numbers) != 3:
        return jsonify({"error": "Please provide exactly 3 numbers"}), 400

    try:
        total = sum(numbers)
        result = (total ** 2) % 10
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/predict_ai", methods=["POST"])
def predict_ai():
    data = request.get_json()
    numbers = data.get("numbers")
    if not numbers or len(numbers) != 3:
        return jsonify({"error": "Please provide 3 numbers"}), 400

    scaler = joblib.load("model/scaler.save")
    model = load_model("model/lottery_model.h5")
    inp = scaler.transform([numbers])
    pred = model.predict(inp)[0]
    predicted_number = int(np.argmax(pred))
    return jsonify({"prediction": predicted_number})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
