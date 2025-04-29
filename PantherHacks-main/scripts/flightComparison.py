class FlightComparison:
    def __init__(self, flights):
        # Takes a list of Flight objects.
        
        self.flights = flights

    def compare_distances(self):
        # Compare the distances traveled by each flight.
        
        print("Distance Comparison (in miles):")
        for flight in self.flights:
            print(f"Flight from {flight.start} to {flight.end}: {flight.distance:,} miles")
        print()

    def compare_fuel_usage(self):
        # Compare total fuel usage (in kg) for each flight.
        
        print("Fuel Usage Comparison (in kg CO₂):")
        for flight in self.flights:
            total_impact = flight.calcImpact()
            print(f"Flight from {flight.start} to {flight.end}: {total_impact:,.2f} kg CO₂")
        print()

    def most_efficient_flight(self):
        # Find the flight with the lowest fuel used per mile.
        
        best_flight = None
        best_efficiency = float('inf')

        for flight in self.flights:
            fuel_used = flight.calcImpact() / 3.1  # reverse carbon to kg fuel
            efficiency = fuel_used / flight.distance  # kg fuel per mile
            if efficiency < best_efficiency:
                best_efficiency = efficiency
                best_flight = flight

        if best_flight:
            print(f"Most efficient flight (least fuel per mile): {best_flight.start} to {best_flight.end}")
            print(f"Efficiency: {best_efficiency:.2f} kg fuel/mile")
        else:
            print("No flights available for comparison.")
