import requests
from twilio.rest import Client


url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your api key"
weather_params = {
    "lat": 44.3735,
    "lon": 17.8153,
    "appid": api_key,
    "cnt": 4,
}

account_sid = "twilio acc sid"
auth_token = "authtoken"

response = requests.get(url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for n in range(0,4):
    weather_id = weather_data["list"][n]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_= "twilio phone number",
        body= "It's going to rain today. Remember to bring an ☔️",
        to= "your number"
    )
    print(message.status)



