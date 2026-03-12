from ai_modules.rainfall_api import get_rainfall

def predict_rainwater(city, roof_area):

    rainfall = get_rainfall(city)

    # formula
    collected_water = roof_area * rainfall * 0.8

    if collected_water > 5000:
        recommendation = "Install large rooftop rainwater harvesting system"

    elif collected_water > 1000:
        recommendation = "Medium storage tank recommended"

    else:
        recommendation = "Small rainwater barrel recommended"

    return {
        "city": city,
        "rainfall_mm": rainfall,
        "estimated_water_liters": collected_water,
        "recommendation": recommendation
    }
