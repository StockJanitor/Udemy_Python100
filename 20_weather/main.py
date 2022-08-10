import requests


MY_LAT = 33.968130
MY_LONG = -117.909752
api_key = "0a7d474222811f0191ce356fe2285e7e"


# url = "https://api.openweathermap.org/data/3.0/onecall"
url="https://api.openweathermap.org/data/2.5/weather"
weather_parameter={
    "lat" : MY_LAT,
    "lon": MY_LONG,
    "appid" : api_key,
}

response = requests.get(url,params=weather_parameter)

response.raise_for_status()

response.json()