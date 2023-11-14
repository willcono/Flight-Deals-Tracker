import requests
import json

with open("config.json", "r+") as raw:
    data = json.load(raw)
SHEETY_ENDPOINT = data["SHEETY_ENDPOINT"]


class DataManager:
    def __init__(self):
        self.base_url = SHEETY_ENDPOINT
        self.bearer = {
            "Authorization": f"Bearer {data['Bearer']}"
        }


    # def get_city(self):
    #     self.response = requests.get(url=self.base_url, headers=self.bearer)
    #     city =
    def get_cities(self):
        response = requests.get(url=self.base_url, headers=self.bearer)
        cities = [location['city'] for location in response.json()['prices'][0:10]]
        return cities

    def get_sheet_data(self):
        response = requests.get(url=self.base_url, headers=self.bearer)
        sheet_data = response.json()['prices']
        return sheet_data

    def add_iata(self, id, iata):
        iata_data = {
            'price': {
                'iataCode': iata
            }
        }
        try:
            response = requests.put(url=f"{self.base_url}/{id}", json=iata_data, headers=self.bearer)
            return response.json()
        except Exception as e:
            return e
    def get_prices(self, iata):
        response = requests.get(url=self.base_url, headers=self.bearer)
        sheet_data = response.json()['prices']['lowestPrice']
        return sheet_data