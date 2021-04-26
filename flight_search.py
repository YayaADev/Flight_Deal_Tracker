import requests
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/Yehya Ahmed/OneDrive/Documents/env.txt")

kiwi_get_url = os.getenv("kiwi_get_url")
kiwi_apikey = os.getenv("kiwi_apikey")


class FlightSearch:
    def __init__(self):
        pass

    def update_iata_code(self, city_name):
        header = {
            "apikey": kiwi_apikey
        }
        kiwi_param = {
            "term": city_name,
            "location_types": "city"
        }
        kiwi_response = requests.get(url=f"{kiwi_get_url}/locations/query", headers=header, params=kiwi_param)
        kiwi_data = kiwi_response.json()["locations"]

        code = kiwi_data[0]["code"]
        return code

    def search_for_flights(self, departure_code, destination_code, from_date, return_date):
        header = {
            "apikey": kiwi_apikey
        }
        param = {
            "fly_from": departure_code,
            "fly_to": destination_code,
            "date_from": from_date,
            "date_to": return_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 21,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "USD",

        }
        response = requests.get(url=f"{kiwi_get_url}/v2/search", headers=header, params=param)
        try:
            response_data = response.json()["data"][0]
        except IndexError:
            return None

        flight_data = FlightData(
            price=response_data["price"],
            origin_city=response_data["route"][0]["cityFrom"],
            origin_airport=response_data["route"][0]["flyFrom"],
            destination_city=response_data["route"][0]["cityTo"],
            destination_airport=response_data["route"][0]["flyTo"],
            day_you_leave=response_data["route"][0]["local_departure"].split("T")[0],
            return_date=response_data["route"][1]["local_departure"].split("T")[0],
            airline=response_data["airlines"]
        )

        return flight_data
