import requests
import json





class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.destination_data = {}
        path_tokens = r"C:\Users\Gumo\Desktop\Git\Projects\Notebook\keys\token.json"    # desktop,
        self.url_sheety = "https://api.sheety.co/ea4e04f3d9056ed487f8bd704c87649f/flightDeals/sheet1"

        # load token and sheety link
        with open (path_tokens,"r") as data:
            self.tokens = json.load(data)

    def get_destination_data(self):
        # requesting data
        response = requests.get(url=self.url_sheety,headers=self.tokens["sheety"])
        # convert feedback to json
        data = response.json()
        # assign sheet1 data
        self.destination_data = data["sheet1"]

        return self.destination_data
    
    def update_destination_codes(self):
        # for each line, city should be already changed
        for city in self.destination_data:
            new_data = { "sheet1":{"iataCode":city["iataCode"]}}
            
            # changing the data 1 be 1, to new city data -> Testing
            response = requests.put(
                url=f"{self.url_sheety}/{city['id']}",
                json=new_data,
                headers=self.tokens["sheety"]
            )
            # print(response.text)