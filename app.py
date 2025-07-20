from flask import Flask, request, jsonify
import math
import os

app = Flask(__name__)

def calculate_next_number(a, b, c):
    total = a + b + c
    result = (total * total) % 10
    return result

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    numbers = data.get("numbers", [])
    
    if len(numbers) < 3:
        return jsonify({"error": "At least 3 numbers are required"}), 400

    a, b, c = numbers[-3], numbers[-2], numbers[-1]
    prediction = calculate_next_number(a, b, c)

    return jsonify({"prediction": prediction})

# ✅ Public Render deployment-compatible server runner
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render will inject PORT
    app.run(host="0.0.0.0", port=port)
