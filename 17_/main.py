from datetime import datetime
import pandas as pd
import random


today = datetime.now()
today_tuple=(today.month,today.day)

path_data =r"C:\Users\Gumo\Desktop\Git\Class\Udemy\17_\birthdays.csv"

data = pd.read_csv(path_data)
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row)in data.iterrows()}

print(birthdays_dict)