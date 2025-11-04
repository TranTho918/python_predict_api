from flask import Flask, request, jsonify
from flask_cors import CORS
from predict_model import predict_stroke

# ============================================================
# Flask App setup
# ============================================================
app = Flask(__name__)
CORS(app)  # Cho phép Shiny (hoặc web khác) truy cập

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "✅ Stroke Prediction API is running."}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        result = predict_stroke(data)
        return jsonify({"success": True, "result": result}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
