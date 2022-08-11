import requests
from bs4 import BeautifulSoup
import pandas as pd

url_news = "https://news.ycombinator.com/"

response = requests.get(url_news)
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")
title_list = soup.find_all(name="a", class_="titlelink")
title_text = [i.getText() for i in title_list]
title_link = [i.get("href") for i in title_list]

score_list = soup.find_all(name="span", class_="score")
score_text = [i.getText() for i in score_list]

dic = {
    "title":title_text,
    "link":title_link,
    
}

print(len(title_text))
print(len(title_link))
print(len(score_text))

print("\n\n\n")


# df=pd.DataFrame(dic)

# # df1 = pd.DataFrame(title_text,columns=["title"])
# # df2 = pd.DataFrame(title_link,columns=["link"])
# df3 = pd.DataFrame(score_text,columns=["score"])
# # mergedf=dataframe2.merge(df1,how="left")
# print(df)
# print(df3)