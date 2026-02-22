import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 68
HEIGHT_CM = 175
AGE = 19

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = os.getenv("sheety_endpoint")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
