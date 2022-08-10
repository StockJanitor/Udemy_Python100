from calendar import different_locale
from urllib import request
import requests

# define variables
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

path_newsapi_key = r"C:\Users\Gumo\Desktop\Git\Notebook\keys\newsapi.txt"
path_alpha_api = r"C:\Users\Gumo\Desktop\Git\Notebook\keys\alphaVantage.txt"

with open(path_newsapi_key,"r") as newsfile:
    key_newsapi = newsfile.readline()
with open(path_alpha_api,"r") as alphafile:
    key_alphaapi = alphafile.readline()

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":key_alphaapi,
}

response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
diff_percent = difference/day_before_yesterday_closing_price * 100

news_params = {
    "apiKey":key_newsapi,
    "qInTitle":COMPANY_NAME,
}

if diff_percent > 3 or diff_percent < -3:
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)


####################### didnt complete but you get the idea...
# then send articles to sms or email