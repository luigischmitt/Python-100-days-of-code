import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = "ACb35c62a9332798021416b5243a19080e"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": -7.119496,
    "lon": -34.845013,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()

data = response.json()

will_rain = False
for i in range(0, 4):
    if data["list"][i]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella!",
                     from_="+17075959294",
                     to="my_number"
                 )
    print(message.status)
