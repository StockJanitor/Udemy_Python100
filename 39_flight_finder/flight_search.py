import json
import requests

class FlightSearch:
    
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        path_tokens = r"C:\Users\Gumo\Desktop\Git\Projects\Notebook\keys\token.json"    # desktop,
        # load token and sheety link
        with open (path_tokens,"r") as data:
            self.tokens = json.load(data)

        self.tequila_url = "https://tequila-api.kiwi.com"
        self.tequila_token = self.tokens["tequila"]

    # https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
    def get_destination_code(self,city_name):
        # request parameters
        url = f"{self.tequila_url}/locations/query"
        header = {"apikey":self.tequila_token}
        query = {"term":city_name, "location_types":"city"}

        #request
        response = requests.get(url=url,headers=header,params=query)
        results = response.json()["locations"]
        code = results[0]["code"]

        return code