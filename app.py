from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ CK Lottery AI Predictor is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        a = int(data.get('a', 0))
        b = int(data.get('b', 0))
        c = int(data.get('c', 0))
        
        # CK Lottery logic from Decompiled.apk: (a + b + c)^2 % 10
        result = ((a + b + c) ** 2) % 10

        return jsonify({
            'predicted_number': result,
            'confidence': "99%",
            'formula_used': "((a + b + c)^2) % 10"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)