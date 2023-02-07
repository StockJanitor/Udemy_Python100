#ventusky - live weather site

import requests
from twilio.rest import Client

# Load key
path_token = r"C:\Users\Gumo\Desktop\Git\notebook\keys\openweather.txt" 
with open(path_token,"r") as newsfile:
    token = newsfile.readlines()


# variables
MY_LAT = 33.968130
MY_LONG = -117.909752
api_key = token

url = "https://api.openweathermap.org/data/2.5/onecall"
# url="https://api.openweathermap.org/data/2.5/weather"
weather_parameter={
    "lat" : MY_LAT,
    "lon": MY_LONG,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}


# variables fot twilio
account_sid=""
auth_token = ""


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