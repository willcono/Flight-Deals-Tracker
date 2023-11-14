from twilio.rest import Client
import json

with open("config.json", "r+") as raw:
    data = json.load(raw)

ACCOUNT_SID = data["ACCOUNT_SID"]
AUTH_TOKEN = data["AUTH_TOKEN"]
TWILIO_NUM = data["TWILIO_NUM"]
MY_NUM = data["MY_NUM"]


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, price, city):
        message = self.client.messages \
            .create(
            body=f"Lower price for {city}: ${price}",
            from_=TWILIO_NUM,
            to=MY_NUM
        )
        return message.status
