import requests
from requests.models import Response
import credential
import json
import datetime



# --------------------- Exercise calories API ------------
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": credential.GetAPPID(),
    "x-app-key": credential.GetAPIKey(),
}

exercise_text = input("Tell me about your exercise : \n")

params = {
    "query":exercise_text,
    "gender":"female",
    "weight_kg":72.5,
    "height_cm":167.64,
    "age":30
}

response = requests.post(url=ENDPOINT,json=params,headers=headers)
result = response.json()
print(result)

# ----------Spreadsheet API -----------

WORKOUT_ENDPOINT =  "https://api.sheety.co/ad05316c37fdbce7984dfb63b2c1d8db/copyOfMyWorkouts/workouts"

#The "workout" sheet enpoint is automatically pluralized on the API end point...

params = {
    "workout":{
        "date": "21/05/27",
        "time": "15:00:01",
        "exercise": "Jogging",
        "duration": "50",
        "calories": "140",
    }
}

auth = {
    "Authorization": "Bearer helloexercise"
}

response = requests.post(url=WORKOUT_ENDPOINT, json=params, headers=auth)
result = response.json()
print(result)