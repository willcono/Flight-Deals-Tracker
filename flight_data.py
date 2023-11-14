import datetime
import requests
import json

with open("config.json", "r+") as raw:
    data = json.load(raw)

FLIGHT_SEARCH_ENDPOINT = data["FLIGHT_SEARCH_ENDPOINT"]
FLIGHT_SEARCH_API = data["FLIGHT_SEARCH_API"]
HOME = "LAX"

class FlightData:

    def __init__(self):
        self.departure_airport_code = "LAX"
        self.base_url = FLIGHT_SEARCH_ENDPOINT
        self.api = FLIGHT_SEARCH_API
        self.today = datetime.date.today() + datetime.timedelta(days=1)
        self.date_from = self.today.strftime("%d/%m/%Y")
        self.future_date = self.today + datetime.timedelta(6 * 30)
        self.date_to = self.future_date.strftime("%d/%m/%Y")
        self.header = {
            "apikey": self.api
        }

    def get_prices(self, iata):
        parameters = {
            "fly_from": self.departure_airport_code,
            "fly_to": iata,
            "date_from": self.date_from,
            "date_to": self.date_to,
        }
        try:
            response = requests.get(url=self.base_url,params=parameters, headers=self.header)
            price = response.json()['data'][0]['price']
            return price
        except Exception as e:
            return e





