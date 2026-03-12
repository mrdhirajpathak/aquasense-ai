def calculate_water_usage(people, showers, washing, cooking):

    shower_usage = showers * 50
    washing_usage = washing * 30
    cooking_usage = cooking * 10

    total_daily = (shower_usage + washing_usage + cooking_usage) * people

    monthly = total_daily * 30

    return {
        "daily_usage_liters": total_daily,
        "monthly_usage_liters": monthly
    }
