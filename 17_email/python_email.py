import datetime as dt
import random
import smtplib
from pass1 import password

now = dt.datetime.now()
weekday = now.weekday()

my_email = "stockjanitor@yahoo.com"
path_quotes = r"C:\Users\Gumo\Desktop\Git\Class\Udemy\17_\quotes.txt"




if weekday ==1:
    with open(path_quotes) as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    # connect to mail server
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    
        # secure the connection
        connection.starttls()
        
        # login
        connection.login(user=my_email, password =password)

        # send mail
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="stockjanitor@gmail.com",
            msg=f"Subject: Quote of the Day\n\n{quote}"
            )
