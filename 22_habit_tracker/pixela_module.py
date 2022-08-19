import requests

class Pixela:

    # insert username and token
    def __init__(self,username,token) -> None:

        self.username = username

        # convert to pixela format
        self.token = {
            "X-USER-TOKEN":token
            }
    

    # update graph takes 3 params
    def update_graph(self, graph_id : str, date : int, amount : float):
        '''graph_id, date-YYYYMMDD, amount --> response and link'''
        
        # convert to pixela format
        params= {
            "date":str(date),
            "quantity":str(amount),
        }
        
        # obtain the url to update the graph
        url = f"https://pixe.la/v1/users/{self.username}/graphs/{graph_id}"
        response = requests.post(url=url,json=params,headers=self.token)

        # print response
        print(response.text)
        print(url+".html")



    # create graph takes 5 arugments, 2 default
    def create_graph(self,id_ : str ,title_ : str, measure_unit:str,color_="sora",types="float"):
        '''id, title, unit, color, type of unit --> response and link; 
        [sora: blue], 
        [shibafu: green], 
        [momiji: red], 
        [ichou: yellow], 
        [ajisai: purple], 
        [kuro: black], 

        '''

        # url to request
        url_create_graph = f"https://pixe.la/v1/users/{self.username}/graphs"
        graph_params = {
            "id" : id_,
            "name" : title_,
            "unit" : measure_unit,
            "type" : types,
            "color" : color_
        }
        response = requests.post(url = url_create_graph, json=graph_params,headers=self.token)
        
        # create graph url
        url = f"https://pixe.la/v1/users/{self.username}/graphs/{graph_params['id']}.html"
        
        # print results
        print(response.text)
        print(url)


    # delete graph
    def delete_graph(self, graph_id : str):
        '''graph id --> response'''
        
        # make url
        url_delete = f"https://pixe.la/v1/users/{self.username}/graphs/{graph_id}"
        response = requests.delete(headers=self.token,url=url_delete)
        
        #print result
        print(response.text)