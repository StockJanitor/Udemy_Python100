import json
import requests
from flight_data import FlightData
from pprint import pprint
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
    
    def check_flights(self,original_city_code,destination_city_code,from_time,to_time):
        
        # parameters
        url = f"{self.tequila_url}/v2/search"
        header = {"apikey":self.tequila_token}
        query = {
            "fly_from":original_city_code,
            "fly_to":destination_city_code,
            "date_from":from_time.strftime("%d/%m/%Y"),
            "date_to":to_time.strftime("%d/%m/%Y"),
            "flight_type":"oneway",
            "curr":"USD",
            "max_stopovers":1
        }

        # request
        response = requests.get(url=url,headers=header,params=query)
        # see if there is data or not
        try:
            data = response.json()["data"][0]
            pprint(data)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        # assign to flgiht data
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"]
        )

        # see if there is out_date, departure date
        try:
            out_date=data["route"][0]["local_departure"].split("T")[0]
            flight_data.out_date = out_date
        except:
            print("out_date no work")

        # see if there is retur date
        try:
            return_date=data["route"][1]["local_departure"].split("T")[0]
            flight_data.return_date = return_date
        except:
            print("return_date no work")
            

        # print out the destination and price
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data