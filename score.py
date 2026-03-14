import json
import numpy as np
import tensorflow as tf
import os

MODEL = None


def load_model():
    """
    Load the TensorFlow model when the deployment container starts.
    """
    global MODEL

    model_path = "water_model.h5"

    if not os.path.exists(model_path):
        raise Exception(f"Model file not found: {model_path}")

    MODEL = tf.keras.models.load_model(model_path)

    print("Water quality model loaded successfully.")

    return MODEL


def score(payload):
    """
    Called by IBM Watson Machine Learning for every prediction request.
    """

    global MODEL

    try:

        # Convert payload string to dictionary if needed
        if isinstance(payload, str):
            payload = json.loads(payload)

        # Validate payload structure
        if "input_data" not in payload:
            return {"error": "Invalid payload. 'input_data' field is missing."}

        input_data = payload["input_data"]

        if not isinstance(input_data, list) or len(input_data) == 0:
            return {"error": "input_data must be a non-empty list."}

        values = input_data[0].get("values")

        if values is None:
            return {"error": "'values' field missing inside input_data."}

        # Convert input values to numpy array
        input_array = np.array(values)

        # Run prediction
        predictions = MODEL.predict(input_array)

        # Convert predictions to list
        predictions_list = predictions.tolist()

        # Return prediction result
        return {
            "predictions": [
                {
                    "values": predictions_list
                }
            ]
        }

    except Exception as e:
        return {"error": str(e)}
