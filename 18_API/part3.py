import requests
from datetime import datetime
import smtplib
from pass1 import password
import time

MY_LAT = 33.968130
MY_LONG = -117.909752

my_email = "stockjanitor@yahoo.com"
is_night = False
if_loop = True

def is_iss_overhead():
    # request
    url="http://api.open-notify.org/iss-now.json"
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()

    #obtain iss lat and long
    iss_latitude =float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True
    
    print(f"my lat {MY_LAT}, my long {MY_LONG}\niss lat {iss_latitude}, iss long {iss_longitude}")


def is_night():
    parameters={
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0,
        }
    url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url,params=parameters,verify=False)
    # response.raise_fot_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = int(datetime.utcnow().hour)
    print(f"time now {time_now},\nsunset {sunset},\nsunrise {sunrise}")
    if (time_now <= sunrise) or (time_now >= sunset):
        return True
    


while if_loop:
    print("\n\n")
    print(f"time now: {datetime.now()}")
    print(f"utc now: {datetime.utcnow()}")
    print("\n")
    if is_night and is_iss_overhead():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        
            # secure the connection
            connection.starttls()
            
            3
            # login
            connection.login(user=my_email, password =password)

            # send mail
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="stockjanitor@gmail.com",
                msg=f"Subject: Lookup\n\nISS is above you in the sky.")
        if_loop=False
    time.sleep(90)