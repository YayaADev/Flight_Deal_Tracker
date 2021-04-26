from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/Yehya Ahmed/OneDrive/Documents/env.txt")

API_KEY = os.getenv("API_KEY")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

my_twilio_number = os.getenv("my_twilio_number")
my_number = os.getenv("my_number")


class NotificationManager:

    def send_sms(self, flight_data):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Flight Deal. ${flight_data.price} to fly from {flight_data.from_city}-{flight_data.origin_airport} to {flight_data.to_city}-{flight_data.destination_airport} from {flight_data.day_you_leave} to {flight_data.return_date}",
            from_=os.getenv("my_twilio_number"),
            to=os.getenv("my_number"))
        print(message.status)
