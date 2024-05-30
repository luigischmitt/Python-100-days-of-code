# WORKOUT TRACKING USING GOOGLE SHEETS

import requests
from datetime import datetime

APP_ID = "my_id"
APP_KEY = "my_key"
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com"
SHETTY_ENDPOINT = "https://api.sheety.co/my_key/myWorkoutsProject/workouts"
USERNAME = "my_user"
PASSWORD = "my_password"

exercises_endpoint = f"{NUTRI_ENDPOINT}/v2/natural/exercise"

exercise_params = {
    "query": str(input("Tell me which exercises you did: ")),
    "age": "19",
    "weight_kg": "57",
    "height_cm": "175"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(url=exercises_endpoint, json=exercise_params, headers=headers)
data = response.json()
data_list = data["exercises"]

today = datetime.now()

for i in range(0, len(data_list)):
    params = { 
        "workout":  {
            "date": f"{today.strftime('%d/%m/%Y')}",
            "time": f"{today.strftime('%X')}",
            "exercise": data["exercises"][i]["name"].title(),
            "duration": data["exercises"][i]["duration_min"],
            "calories": data["exercises"][i]["nf_calories"],
            "id": data["exercises"][i]["tag_id"]
        }
    }

    new_response = requests.post(url=SHETTY_ENDPOINT, json=params, headers=headers, auth=(USERNAME, PASSWORD))
    print(new_response.json())


