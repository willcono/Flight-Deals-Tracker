from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

fs = FlightSearch()
dm = DataManager()
fd = FlightData()
nm = NotificationManager()
sheet_data = dm.get_sheet_data()
for location in sheet_data:
    iata = location['iataCode']
    city = location['city']
    price = location['lowestPrice']
    flight_price = fd.get_prices(iata=iata)
    if price > flight_price:
        print(city, flight_price)
        nm.send_message(city=city, price=flight_price)



