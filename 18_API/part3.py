import requests
from datetime import datetime
import smtplib
from pass1 import password
import time

MY_LAT = 33.968130
MY_LONG = -117.909752

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

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True




my_email = "stockjanitor@yahoo.com"
while True:
    time.sleep(90)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        
            # secure the connection
            connection.starttls()
            
            # login
            connection.login(user=my_email, password =password)

            # send mail
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="stockjanitor@gmail.com",
                msg=f"Subject: Lookup\n\nISS is above you in the sky.")