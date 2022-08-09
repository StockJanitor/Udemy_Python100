from datetime import datetime
import pandas as pd
import random
import smtplib
from pass1 import password

my_email = "stockjanitor@yahoo.com"
today = datetime.now()
today_tuple=(today.month, today.day)

path_data =r"C:\Users\Gumo\Desktop\Git\Class\Udemy\17_\birthdays.csv"
path_letter = r"C:\Users\Gumo\Desktop\Git\Class\Udemy\17_\letter_templates\letter_"
data = pd.read_csv(path_data)
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row)in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"{path_letter}{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # connect to mail server
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    
        # secure the connection
        connection.starttls()
        
        # login
        connection.login(user=my_email, password =password)

        # send mail
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!!\n\n{contents}"
            )

# Python anywhere