from flight import Flight
import requests
import os
import json


# https://aviationstack.com/documentation

class Routes:
    def __init__(self, flight):
        self.start = flight.start
        self.end = flight.end
        self.flightList = [flight]
        self.distance = flight.distance
        self.flightStackUrl  = "https://api.aviationstack.com/v1/flights"

    def pullRouteFlights(self):
        access_key = os.getenv('AVIATIONSTACK_API_KEY')
        queryString = {
            "dep_icao": self.flightList[0].start,
            "arr_icao": self.flightList[0].end,
            "access_key":access_key
        }
        response = requests.get(self.flightStackUrl, params=queryString)

        if response.status_code != 200:
            print(f"Error fetching flights: {response.status_code}")
            return

        data = response.json()
        flights = data.get('data', [])
        print("POST DATA")

        for flight in flights:
            flight_icao = flight['flight']['icao']
            print("ICAO DATA")
            print(flight_icao)
            if flight_icao == self.flightList[0].flightID:
                continue

            print("POST FLIGHT GET")
            print(f"Distance: {self.distance}")

            print("PRE ADD FLIGHT")
            self.addToFlightList(Flight(flight_icao, self.flightList[0].date, self.distance))


    def addToFlightList(self, flight):
        if flight.start == self.start and flight.end == self.end:
            print("FLIGHT PARAM CHECK")
            self.flightList.append(flight)
        else:
            print(f"Flight {flight.flightID} from {flight.start} to {flight.end} doesn't match expected route {self.start} ➔ {self.end}")

    def consolidate(self):  
        totalSeats = 0 
        totalPassengers = 0
        for flight in self.flightList:
            totalSeats += int(flight.plane.seats)
            totalPassengers += int(flight.plane.passengers)

        totalFillRatio = totalPassengers/totalSeats
        print(f"The total fill ratio of filled seats from {self.start} to {self.end} is {totalFillRatio:.2f}")

        sortedflightList = sorted(self.flightList, key=lambda flight: flight.plane.seats, reverse=True)
        usedflights = []
        remainingPassengers = totalPassengers

        for flight in sortedflightList:
            if remainingPassengers <= 0:
                break
            if int(flight.plane.seats) >= remainingPassengers:
                remainingPassengers = 0
                usedflights.append(flight)
            else: 
                usedflights.append(flight)
                remainingPassengers -= int(flight.plane.passengers)

        print(f"Minimum flights needed: {len(usedflights)}")
        print(f"Flights used: {[f.flightID for f in usedflights]}")
        print(f"Planes used: {[f.plane.model for f in usedflights]}")
        return usedflights

        
    def compareCarbon(self, newflightList): # returns better flight list
        if len(self.flightList) == len(newflightList):
            print(f"There is no optimal way to redistribute flights for flights from {self.flightList[0].start} to {self.flightList[0].end}")
            return self.flightList
        
        oldCarbon = 0
        oldCarbonCapita = 0
        oldFuel = 0
        totalPassengers = 0
        for flight in self.flightList:
            oldCarbon += flight.calcImpact()
            oldCarbonCapita += flight.calcImpactPerCapita()
            oldFuel += flight.plane.fuel
            totalPassengers += flight.plane.passengers

        oldFuelPerPass = totalPassengers / oldFuel

        print(f"The old Fuel per Passenger is {oldFuelPerPass:.2f}\nThe old Carbon Impact is {oldCarbon} and per cap is: {oldCarbonCapita}")

        newCarbon = 0
        newCarbonCapita = 0
        newFuel = 0
        for flight in newflightList:
            newCarbon += flight.calcImpact()
            newCarbonCapita += flight.calcImpactPerCapita()
            newFuel += flight.plane.fuel

        newFuelPerPass = totalPassengers / newFuel

        #TODO ADD UNITS
        print(f"""Comparing Carbon: \nNew emmissions are lower by {oldCarbon - newCarbon}! 
              \nEmmisions per capita have been lowered by {oldCarbonCapita - newCarbonCapita}!
              \nThe overall fuel per passenger has been lowered to {newFuelPerPass}!
                """)
        
        return newflightList

    def get_similar_flights_data(self):
        # Get up to 4 flights from the list (excluding the main flight if needed)
        flights = self.flightList[:4]
        result = []
        for flight in flights:
            result.append({
                "carbonReduction": None,  # Placeholder, can be calculated if needed
                "planeModel": getattr(flight.plane, "model", None),
                "flightNum": getattr(flight, "flightID", None),
                "emissionsPerPerson": getattr(flight.calcImpactPerCapita, "impactPerCapita", None),
            })
        # Pad to 4 if less than 4 flights
        while len(result) < 4:
            result.append({
                "carbonReduction": None,
                "planeModel": None,
                "flightNum": None,
                "emissionsPerPerson": None,
            })
        return result

route = Routes(Flight('AAL81','2025-04-27'))
route.pullRouteFlights()
route.compareCarbon(route.consolidate())