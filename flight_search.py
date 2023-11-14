import requests
import json

with open("config.json", "r+") as raw:
    data = json.load(raw)
FLIGHT_SEARCH_ENDPOINT = data["FLIGHT_SEARCH_ENDPOINT"]
FLIGHT_SEARCH_API = data["FLIGHT_SEARCH_API"]


class FlightSearch:

    def __init__(self):
        self.base_url = FLIGHT_SEARCH_ENDPOINT
        self.api = FLIGHT_SEARCH_API
        self.header = {
            "apikey": self.api
        }

    def get_iata(self, city):
        url = self.base_url
        api = self.header
        parameters = {
            "term": city
        }
        response = requests.get(url=url, params=parameters, headers=api)
        iata = response.json()['locations'][0]['code']
        return iata
