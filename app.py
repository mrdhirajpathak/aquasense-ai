from flask import Flask, request, jsonify, render_template
import os
import gdown
from config import (
    IBM_API_KEY,
    IBM_PROJECT_ID,
    IBM_URL,
    MODEL_ID,
    UPLOAD_FOLDER,
    MODEL_PATH
)

# AI Modules
from ai_modules.watsonx_ai import ask_watson
from ai_modules.rainwater_predictor import predict_rainwater
from ai_modules.crisis_model import predict_crisis
from ai_modules.image_detection import detect_pollution


# ---------------- FLASK APP ----------------

app = Flask(__name__)


# ---------------- MODEL DOWNLOAD ----------------

if not os.path.exists(MODEL_PATH):

    os.makedirs("models", exist_ok=True)

    url = "https://drive.google.com/uc?id=1Af0frb358OHWFDupuicc89f_h8fmDw5h"

    print("Downloading water prediction model...")

    gdown.download(url, MODEL_PATH, quiet=False)


# ---------------- UPLOAD FOLDER ----------------

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- MAP PAGE ----------------

@app.route("/map")
def mapview():
    return render_template("map.html")


# ---------------- AI CHATBOT ----------------

@app.route("/ask", methods=["POST"])
def ask():

    data = request.json

    question = data.get("question")

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

    city = data.get("city")
    area = data.get("area")

    result = predict_rainwater(city, area)

    return jsonify(result)


# ---------------- WATER CRISIS PREDICTION ----------------

@app.route("/predict-crisis", methods=["POST"])
def crisis():

    data = request.json

    rainfall = float(data.get("rainfall"))
    population = float(data.get("population"))
    consumption = float(data.get("consumption"))
    groundwater = float(data.get("groundwater"))

    result = predict_crisis(
        rainfall,
        population,
        consumption,
        groundwater
    )

    return jsonify({
        "prediction": result
    })


# ---------------- IMAGE POLLUTION DETECTION ----------------

@app.route("/upload", methods=["POST"])
def upload():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    result = detect_pollution(filepath)

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

    people = int(data.get("people"))
    showers = int(data.get("showers"))
    laundry = int(data.get("laundry"))

    daily_usage = (people * 135) + (showers * 50) + (laundry * 70)
    monthly_usage = daily_usage * 30

    return jsonify({
        "daily_usage_liters": daily_usage,
        "monthly_usage_liters": monthly_usage
    })


# ---------------- SERVER RUN ----------------

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
