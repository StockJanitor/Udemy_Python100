#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


from data_manager import DataManager as dm
from datetime import datetime, timedelta
from flight_search import FlightSearch
# obtaining data
data_manager = dm()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)
flight_search=FlightSearch()

######################## inputs ########################
ORIGIN_CITY_IATA = "LAX"
# obtain the dates
tomorrow = datetime.now() + timedelta(days=20)
print(tomorrow)
six_month_from_today = datetime.now() + timedelta(days=(25))
print(six_month_from_today)



# check if iataCode exist
if sheet_data[0]["iataCode"] == "":
    # set sheet_data every iataCode to Testing
    for row in sheet_data:
        # set the iataCode to flight_search.get_destination_code
        row["iataCode"]=flight_search.get_destination_code(row["city"])
    # print(f"sheet data: {sheet_data}")
    # change data manager data to above new data
    data_manager.destination_data = sheet_data
    # updating the data
    data_manager.update_destination_codes()



# returns the flightData object and prints them
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )