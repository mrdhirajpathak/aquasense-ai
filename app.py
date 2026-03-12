from flask import Flask, request, jsonify, render_template
from ai_modules.watsonx_ai import ask_watson
from ai_modules.rainwater_predictor import predict_rainwater
from ai_modules.crisis_model import predict_crisis
from ai_modules.image_detection import detect_pollution
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/map")
def mapview():
    return render_template("map.html")


# ---------------- AI CHATBOT ----------------

@app.route("/ask", methods=["POST"])
def ask():

    question = request.json["question"]

    answer = ask_watson(
        question,
        "You are an expert AI assistant focused on water conservation, pollution awareness and rainwater harvesting."
    )

    return jsonify({
        "answer": answer
    })


# ---------------- RAINWATER HARVESTING ----------------

@app.route("/rainwater", methods=["POST"])
def rainwater():

    data = request.json

    result = predict_rainwater(
        data["city"],
        data["area"]
    )

    return jsonify(result)


# ---------------- WATER CRISIS PREDICTION ----------------

@app.route("/predict-crisis", methods=["POST"])
def crisis():

    data = request.json

    result = predict_crisis(
        data["rainfall"],
        data["population"],
        data["consumption"],
        data["groundwater"]
    )

    return jsonify({
        "prediction": result
    })


# ---------------- IMAGE POLLUTION DETECTION ----------------

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(path)

    result = detect_pollution(path)

    return jsonify({
        "result": result
    })


# ---------------- HEATMAP DATA ----------------

@app.route("/pollution-data")
def pollution():

    data = [
        [28.61,77.20,0.8],
        [19.07,72.87,0.7],
        [13.08,80.27,0.9],
        [22.57,88.36,0.6],
        [12.97,77.59,0.65]
    ]

    return jsonify(data)


# ---------------- WATER USAGE CALCULATOR ----------------

@app.route("/calcWater", methods=["POST"])
def water_usage():

    data = request.json

    people = int(data["people"])
    showers = int(data["showers"])
    laundry = int(data["laundry"])

    daily_usage = (people * 135) + (showers * 50) + (laundry * 70)
    monthly_usage = daily_usage * 30

    return jsonify({
        "daily_usage_liters": daily_usage,
        "monthly_usage_liters": monthly_usage
    })


# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)