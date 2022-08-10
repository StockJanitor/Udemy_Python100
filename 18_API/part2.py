import requests
from datetime import datetime

url = "https://api.sunrise-sunset.org/json"

MY_LAT = 33.968130
MY_LONG = -117.909752
parameters={
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
    }


response = requests.get(url,params=parameters,verify=False)

# response.raise_fot_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.utcnow()


print(sunrise)
print(sunset)
print(time_now.hour)