import requests
from datetime import datetime

url = "https://api.sunrise-sunset.org/json"


parameters={
    "lat" : 51.5,
    "lng" : -0.12,
    "formatted" : 0,
    }


response = requests.get(url,params=parameters,verify=False)

# response.raise_fot_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


print(sunrise)
print(sunset)
print(time_now.hour)