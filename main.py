import data_manager
import flight_search
from pprint import pprint
import datetime
import notification_manager

data = data_manager.DataManager()
flights = flight_search.FlightSearch()
sheet_data = data.get_sheet_data()
notification = notification_manager.NotificationManager()
origin_city = "NYC"
# Using dates from now till 6 months

today = datetime.datetime.today() + datetime.timedelta(days=1)
tomorrow = today.strftime("%d/%m/%Y")
six_months = datetime.datetime.now() + datetime.timedelta(days=6 * 30)
six_months = six_months.strftime("%d/%m/%Y")


def replace_empty_iata():
    for values in sheet_data:
        if values[1] == "":
            # Get the city name
            flight_city = values[0]
            # changing the IATA code in sheet_data to the code
            values[1] = flights.update_iata_code(flight_city)
    pprint(sheet_data)
    data.sheet_data = sheet_data
    data.update_iatacode()


def flights_per_city():
    for values in sheet_data:
        flight = flights.search_for_flights(origin_city, values[1], tomorrow, six_months)
        # If flight is None that means no flights were found.
        if flight is not None and flight.price < int(values[2]):
            notification.send_sms(flight)


replace_empty_iata()
flights_per_city()
