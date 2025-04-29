import sys
import json
from flight import Flight
from routes import Routes

def main():
    input_data = sys.stdin.read()
    user_input = json.loads(input_data)
    
    num = user_input.get("flight_number")
    date = user_input.get("date")

    origin_code = "OOO"
    destination_code = "OOO"
    origin_full = "Origin"
    destination_full = "Destination"
    plane = "Plane"
    airline = "Airline"
    ppl_count = "0"
    distance = "0"
    net_co2 = "0"
    single_co2 = "0"

    flight = Flight(num, date)
    routes = Routes(flight)
    similar_flights = routes.get_similar_flights_data()

    # Similar flights placeholder (nulls/0s)
    similar_flights = [
        {
            "carbonReduction": None,
            "planeModel": None,
            "flightNum": None,
            "emissionsPerPerson": None,
        },
        {
            "carbonReduction": None,
            "planeModel": None,
            "flightNum": None,
            "emissionsPerPerson": None,
        },
        {
            "carbonReduction": None,
            "planeModel": None,
            "flightNum": None,
            "emissionsPerPerson": None,
        },
        {
            "carbonReduction": None,
            "planeModel": None,
            "flightNum": None,
            "emissionsPerPerson": None,
        },
    ]

    result = {
        "origin_code": flight.start,
        "destination_code": flight.end,
        "origin_full": flight.start_full,
        "destination_full": flight.end_full,
        "date": date,
        "flight_num": num,
        "plane": flight.plane.model,
        "airline": flight.plane.airline,
        "ppl_count": flight.plane.passenger,
        "distance": f"{flight.distance:.3f}",
        "net_co2": flight.carbonImpact,
        "single_co2": flight.impactPerCapita,
        "similar_flights": similar_flights
    }
    print(json.dumps(result))

if __name__ == "__main__":
    main()