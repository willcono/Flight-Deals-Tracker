# Flight-Deals-Tracker
Tracks flights specified from user via IATA code and texts user when price drops below the set price within the next 6 months specified by user in a google sheet.



# Create a config.json file and add the following keys and values:
{
  "FLIGHT_SEARCH_ENDPOINT": "https://api.tequila.kiwi.com/v2/search",
  "FLIGHT_SEARCH_API": "Your tequila.kiwi api",
  "ACCOUNT_SID": "Your Twilio account sid",
  "AUTH_TOKEN": "Your Twilio auth token",
  "TWILIO_NUM": "+Your Twilio number",
  "MY_NUM": "+Your actual phone number",
  "SHEETY_ENDPOINT": "Your Sheety endpoint", 
  "Bearer": "Your Sheety Bearer token
}


# In flight_data.py
Change HOME variable to the IATA of your home airport(This will be the from location)
