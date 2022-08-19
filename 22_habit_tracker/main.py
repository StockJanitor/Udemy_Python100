# from urllib import response
import requests
from datetime import datetime
today = datetime.now()
today = today.strftime("%Y%m%d")
donuts = "210"
USERNAME ="stockjanitor"
TOKEN = ""
headers={
    "X-USER-TOKEN":TOKEN
}

url_create_user = "https://pixe.la/v1/users"
url_create_graph = f"https://pixe.la/v1/users/{USERNAME}/graphs"

################### create an account request and params ###################
user_params = {
    "token": "",
    "username": "stockjanitor",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# response = requests.post(url,json=user_params)
# print(response.text)



################### create graph request and params ###################
graph_params = {
    "id" : "steak",
    "name" : "Steak Activities",
    "unit" : "steaks",
    "type" : "float",
    "color" : "shibafu"
}
response = requests.post(url = url_create_graph, json=graph_params,headers=headers)
print(response.text)



################### upload pixel and params ###################
url_post_pixel = f"{url_create_user}/{USERNAME}/graphs/{graph_params['id']}"

post_pixel_params = {
    "date":today,
    "quantity": donuts

}
# response = requests.post(url=url_post_pixel,json=post_pixel_params,headers=headers)
# print(response.text)


#~~~ edit graph ~~~#
edit_graph_params={
    "color":"sora"
}
# response = requests.put(url_post_pixel,json=edit_graph_params,headers=headers)
# print(response.text)




################### delete graph and params ###################
# url_delete = f"{url_create_user}/{USERNAME}/graphs/{graph_params['id']}/20220810"
# response = requests.delete(headers=headers,url=url_delete)
# print(response.text)

print(f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_params['id']}.html")
# print(today)