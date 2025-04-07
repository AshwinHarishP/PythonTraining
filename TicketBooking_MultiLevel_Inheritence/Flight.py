class Flight:
    flights = []
    def __init__(self, fid, fname, source, destination, ticket_price, age):
        self.fid = fid
        self.fname = fname
        self.source = source
        self.destination = destination
        self.ticket_price = ticket_price
        self.age = age

    def add_flight(self, flightObj):
        Flight.flights.append(flightObj)
        return "Flight Added"

    def display_flight_details():
        if len(Flight.flights) == 0:
            print("No flights available.")
        else:
            for flight in Flight.flights:
                print(f"Flight ID: {flight.fid}")
                print(f"Flight Name: {flight.fname}")
                print(f"Source: {flight.source}")
                print(f"Destination: {flight.destination}")
                print(f"Ticket Price: {flight.ticket_price}")
                print("-" * 50)

    

