import joblib

# Load trained ML model
model = joblib.load("data/water_crisis_model.pkl")

def predict_crisis(rainfall, population, consumption, groundwater):

    input_data = [[rainfall, population, consumption, groundwater]]

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        risk = "High Water Crisis Risk"
    else:
        risk = "Low Water Crisis Risk"

    return {
        "prediction": risk,
        "probability": float(probability)
    }
