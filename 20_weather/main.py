#ventusky - live weather site

import requests
from twilio.rest import Client

# variables
MY_LAT = 33.968130
MY_LONG = -117.909752
api_key = "0a7d474222811f0191ce356fe2285e7e"

url = "https://api.openweathermap.org/data/2.5/onecall"
# url="https://api.openweathermap.org/data/2.5/weather"
weather_parameter={
    "lat" : MY_LAT,
    "lon": MY_LONG,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}


# variables fot twilio
account_sid="AC9deba8e6c590fdb6f488552ae91636f3"
auth_token = "2f1eed22c7718400bb658b46a3f4e749"


# get request
response = requests.get(url,params=weather_parameter)
response.raise_for_status()
weather_data = response.json()

# parse out json
weather_slice = weather_data["hourly"][:12]

# determine if rain
will_rain = False

# loop list
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(600)<700:
        will_rain = True

# print out feedback
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Its going to rain today",
                     from_='+12133184231',
                     to='+18184466008'
                 )

    print(message.status)