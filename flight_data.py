# Contains the information about each flight
class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, day_you_leave,
                 return_date, airline):
        self.price = price
        self.from_city = origin_city
        self.origin_airport = origin_airport
        self.to_city = destination_city
        self.destination_airport = destination_airport
        self.day_you_leave = day_you_leave
        self.return_date = return_date
        self.airline = airline
