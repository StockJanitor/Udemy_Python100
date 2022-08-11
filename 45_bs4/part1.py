'''
# to get text

item.name
item.get("class")
item.getText()
item.get("href")


# finding object
soup.find(name="h1",id="name")
soup.find(name="h3", class_ = "heading")





# CSS Selector
soup.select_one(selector="p a")

soup.select_one(selector="#name")




'''


from bs4 import BeautifulSoup
import os

# get cwd
path = os.getcwd() + r"\45_bs4\website.html"

# read file
with open(path, encoding="utf8") as item:
    contents = item.read()

# create object bs4
soup=BeautifulSoup(contents, 'html.parser')

all_tag = soup.find_all(name="a")
# print(all_tag)


for i in all_tag:
    # print(i.get("href"))
    pass

heading = soup.find(name="h1",id="name")
# print(heading)


section_heading = soup.find(name="h3", class_ = "heading")
# print(section_heading)

compnay_url = soup.select_one(selector="p a")

my_name=soup.select_one(selector="#name")

heading = soup.select(".heading")
print(heading)



# print(my_name)