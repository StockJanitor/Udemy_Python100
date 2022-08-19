import requests

class Pixela:
    def __init__(self,username,token) -> None:
        self.username = username
        self.token = {
            "X-USER-TOKEN":token
            }
    


    def update_graph(self,graph_id : str, date : int, amount : float):
        '''graph_id, date-YYYYMMDD, amount --> feedback and link'''
        params= {
            "date":str(date),
            "quantity":str(amount),
        }
        url = f"https://pixe.la/v1/users/{self.username}/graphs/{graph_id}"
        response = requests.post(url=url,json=params,headers=self.token)
        print(response.text)
        print(url+".html")

    def create_graph(self,id_ : str ,title_ : str, unit_:str,color_="sora",types="float"):
        '''id, title, unit, color, type of unit --> feedback and link'''
        url_create_graph = f"https://pixe.la/v1/users/{self.username}/graphs"
        graph_params = {
            "id" : id_,
            "name" : title_,
            "unit" : unit_,
            "type" : types,
            "color" : color_
        }
        response = requests.post(url = url_create_graph, json=graph_params,headers=self.token)
        url = f"https://pixe.la/v1/users/{self.username}/graphs/{graph_params['id']}.html"
        print(response.text)
        print(url)