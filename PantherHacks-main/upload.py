import sys
import json
from flight import Flight

def main():
    # input_data = sys.stdin.read()
    # user_input = json.loads(input_data)

    
    # num = user_input.get("flight_number")
    # date = user_input.get("date")

    num = input("Enter flight number: ")
    date = input("Enter date (YYYY-MM-DD): ")

    origin_code = "SFO"
    destination_code = "LAX"
    origin_full = "San Francisco"
    destination_full = "Los Angeles"
    plane = "Boeing 787-9 Dreamliner"
    airline = "United Airlines"
    ppl_count = "250"
    distance = "8,000"
    net_co2 = "200"
    single_co2 = "0.192"

    flight = Flight(num, date)
    try:
        flight = Flight(num, date)
    except ValueError as e:
        print(f"Error: {e}")
    return

    flight.getDistance()
    flight.calcImpact()
    flight.calcImpactPerCapita()

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
        "distance": flight.distance,
        "net_co2": flight.carbonImpact,
        "single_co2": flight.impactPerCapita
    }
    print(json.dumps(result))

if __name__ == "__main__":
    main()