#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


from data_manager import DataManager as dm


# obtaining data
data_manager = dm()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

# check if iataCode exist
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search=FlightSearch()

    # set sheet_data every iataCode to Testing
    for row in sheet_data:
        # set the iataCode to flight_search.get_destination_code
        row["iataCode"]=flight_search.get_destination_code(row["city"])
    # print(f"sheet data: {sheet_data}")
    # change data manager data to above new data
    data_manager.destination_data = sheet_data

    # updating the data
    data_manager.update_destination_codes()