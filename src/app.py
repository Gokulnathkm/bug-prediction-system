from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

model = joblib.load("models/model.pkl")

df = pd.read_csv("data/processed/features.csv")
feature_cols = [col for col in df.columns if col not in ["filename", "label"]]


@app.route("/")
def home():
    return "Bug Prediction API Running"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Build row using exact training columns
    row = []
    for col in feature_cols:
        row.append(data.get(col, 0))

    prob = model.predict_proba([row])[0][1]

    risk = "HIGH" if prob > 0.7 else "MEDIUM" if prob > 0.4 else "LOW"

    return jsonify({
        "expected_features": feature_cols,
        "values_used": row,
        "bug_probability": round(float(prob), 4),
        "risk_level": risk
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

