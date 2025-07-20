from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "✅ CK AI BOT API is running! Use POST /predict with numbers."

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
