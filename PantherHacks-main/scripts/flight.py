import mysql.connector
import os
from dotenv import load_dotenv
import requests
import json
from plane import Plane
import sys

load_dotenv()

#connects the db to python code
mydb = mysql.connector.connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USERNAME'),
    password = os.getenv('MYSQL_PASSWORD'),
    auth_plugin = 'mysql_native_password'
    )
# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("USE flightTracker")

access_key = os.getenv('AVIATIONSTACK_API_KEY')
fdp_key = os.getenv('FDP_API_KEY')
air_key = os.getenv('AIRCRAFTDB_API_KEY')

# https://aviationstack.com/documentation
# https://flightplandatabase.com/dev/api#endpoint-create-plan

default_aircraft_by_airline = {
    # Africa
    'ETH': 'B788',  # Ethiopian Airlines (uses 787-8 and 777s)
    'MSR': 'B738',  # EgyptAir (738, A320)
    'SAA': 'A332',  # South African Airways (A330)
    'KQA': 'B738',  # Kenya Airways (738 and 787)
    'RAM': 'B738',  # Royal Air Maroc (737-800)
    'DAH': 'B738',  # Air Algérie (738)
    'TAR': 'A320',  # Tunisair (A320)
    'MAU': 'A332',  # Air Mauritius (A330)
    'APK': 'E145',  # Air Peace (smaller regional jets too)
    'RWD': 'CRJ',   # RwandAir (CRJ, 737)
    'ATC': 'DHC8',  # Air Tanzania (Dash 8 Q400)
    'SFR': 'B738',  # FlySafair (B738 low-cost)
    'AFW': 'ERJ145',# Africa World Airlines (small jets)
    'LAA': 'A320',  # Libyan Airlines
    'VRE': 'A319',  # Air Côte d'Ivoire
    'DTA': 'B738',  # TAAG Angola (B737-700)
    'SGG': 'A319',  # Air Senegal
    'LNK': 'E170',  # Airlink
    'FJW': 'E190',  # Fastjet
    'NIA': 'A320',  # Nile Air

    # Major US
    'AAL': 'B738',
    'DAL': 'A321',
    'UAL': 'B739',
    'SWA': 'B737',
    'ASA': 'B738',  # Alaska Airlines
    'JBU': 'A320',  # JetBlue
    'NKS': 'A320',  # Spirit Airlines
    'FFT': 'A320',  # Frontier
    'AAY': 'A319',  # Allegiant
    'HAL': 'A332',  # Hawaiian Airlines

    # Canada/Mexico
    'ACA': 'B789',  # Air Canada
    'WJA': 'B738',  # WestJet
    'TSC': 'A330',  # Air Transat
    'FLE': 'B737',  # Flair Airlines
    'POE': 'E190',  # Porter Airlines

    # Latin America
    'AMX': 'B738',  # Aeromexico
    'VOI': 'A320',  # Volaris
    'VIV': 'A320',  # VivaAerobus
    'TAO': 'AT72',  # Aeromar (smaller planes)

    'LAN': 'B789',  # LATAM Airlines (787-9)
    'AVA': 'A320',  # Avianca
    'GLO': 'B738',  # GOL
    'AZU': 'E195',  # Azul Brazilian
    'ARG': 'B738',  # Aerolíneas Argentinas
    'SKU': 'A320',  # Sky Airline
    'JAT': 'A320',  # Jetsmart
    'VVC': 'A320',  # Viva Colombia
    'AZP': 'A320',  # Viva Air Peru
    'VCV': 'B737',  # Conviasa (small Boeing jets)

    # Asia
    'CCA': 'A333',  # Air China
    'CES': 'A330',  # China Eastern
    'CSN': 'A320',  # China Southern
    'CHH': 'A320',  # Hainan Airlines
    'CSZ': 'A320',  # Shenzhen Airlines

    'ANA': 'B788',  # All Nippon Airways
    'JAL': 'B788',  # Japan Airlines
    'APJ': 'A320',  # Peach Aviation
    'SKY': 'B737',  # Skymark Airlines
    'JJP': 'A320',  # Jetstar Japan

    'KAL': 'B77W',  # Korean Air
    'AAR': 'A333',  # Asiana Airlines
    'JJA': 'B738',  # Jeju Air
    'TWB': 'B738',  # T'way Air
    'JNA': 'B738',  # Jin Air

    'IGO': 'A320',  # IndiGo
    'AIC': 'B788',  # Air India
    'VTI': 'A320',  # Vistara
    'SEJ': 'B737',  # SpiceJet
    'GOW': 'B737',  # GoFirst

    'SIA': 'B77W',  # Singapore Airlines
    'TGW': 'A320',  # Scoot

    'MAS': 'A330',  # Malaysia Airlines
    'AXM': 'A320',  # AirAsia
    'FFM': 'AT72',  # Firefly

    'THA': 'A350',  # Thai Airways
    'BKP': 'A320',  # Bangkok Airways
    'AIQ': 'A320',  # Thai AirAsia

    'HVN': 'A321',  # Vietnam Airlines
    'VJC': 'A320',  # VietJet Air

    'PAL': 'A330',  # Philippine Airlines
    'CEB': 'A320',  # Cebu Pacific

    'GIA': 'B738',  # Garuda Indonesia
    'LNI': 'B737',  # Lion Air
    'BTK': 'A320',  # Batik Air
    'CTV': 'A320',  # Citilink

    'CPA': 'A359',  # Cathay Pacific
    'CRK': 'A320',  # Hong Kong Airlines
    'HKE': 'A320',  # HK Express

    'CAL': 'A333',  # China Airlines
    'EVA': 'B77W',  # EVA Air
    'SJX': 'A321',  # Starlux

    'AMU': 'A320',  # Air Macau

    'BBC': 'DHC8',  # Biman Bangladesh Airlines
    'UBG': 'ATR72', # US-Bangla Airlines
    'NVQ': 'ATR72', # NovoAir

    'PIA': 'B777',  # Pakistan International Airlines
    'ABQ': 'A320',  # Airblue
    'SEP': 'B737',  # SereneAir

    # Central Asia
    'KZR': 'B738',  # Air Astana
    'VSV': 'B738',  # SCAT Airlines
    'MGL': 'B737',  # MIAT Mongolian Airlines
    'MML': 'ATR72', # Hunnu Air
    'KHV': 'ATR72', # Cambodia Angkor Air
    'MKR': 'A320',  # Lanmei Airlines
    'LAO': 'AT72',  # Lao Airlines
    'UBA': 'ATR72', # Myanmar National Airlines
    'KBZ': 'ATR72', # Air KBZ
    'RNA': 'ATR72', # Nepal Airlines
    'HIM': 'A320',  # Himalaya Airlines

    # South Asia
    'ALK': 'A332',  # SriLankan Airlines
    'AFG': 'B737',  # Ariana Afghan Airlines
    'KMF': 'B737',  # Kam Air
    'SMR': 'B737',  # Somon Air

    'UZB': 'B752',  # Uzbekistan Airways
    'TUA': 'B738',  # Turkmenistan Airlines
    'AHY': 'A320',  # Azerbaijan Airlines

    # Europe
    'DLH': 'A320',  # Lufthansa
    'BAW': 'A320',  # British Airways
    'AFR': 'A320',  # Air France
    'KLM': 'B738',  # KLM
    'RYR': 'B738',  # Ryanair
    'EZY': 'A320',  # EasyJet
    'THY': 'B77W',  # Turkish Airlines
    'SWR': 'A333',  # Swiss Air
    'SAS': 'A320',  # Scandinavian Airlines
    'ITY': 'A320',  # ITA Airways (ex-Alitalia)
    'TAP': 'A320',  # TAP Portugal
    'FIN': 'A320',  # Finnair
    'EIN': 'A320',  # Aer Lingus
    'WZZ': 'A320',  # Wizz Air
    'NAX': 'B738',  # Norwegian
    'BEL': 'A320',  # Brussels Airlines
    'AUA': 'A320',  # Austrian Airlines
    'LOT': 'E195',  # LOT Polish Airlines
    'IBE': 'A320',  # Iberia
    'VLG': 'A320',  # Vueling

    # Australia/Oceania
    'QFA': 'B738',  # Qantas
    'VOZ': 'B738',  # Virgin Australia
    'JST': 'A320',  # Jetstar
    'ANZ': 'B789',  # Air New Zealand

    'FJI': 'A330',  # Fiji Airways
    'ANG': 'ATR72', # Air Niugini
    'AVN': 'ATR72', # Air Vanuatu
    'ACI': 'A320',  # Aircalin
    'THT': 'B787',  # Air Tahiti Nui
    'VTA': 'AT72',  # Air Tahiti
    'SOL': 'DHC8',  # Solomon Airlines
    'AKL': 'DHC8',  # Air Kiribati
    'RON': 'B737',  # Nauru Airlines
    'PAO': 'B737',  # Palau Pacific Airways
    'RAR': 'AT72',  # Air Rarotonga
    'NFA': 'DHC6',  # Norfolk Air
    'MRS': 'DHC8',  # Air Marshall Islands
    'PPA': 'B737',  # Northern Mariana Airways
    'RLT': 'DHC8',  # Real Tonga
    'NMA': 'DHC6',  # Northern Mariana Airways (again?)

}


class Flight:
        def __init__(self, flightID, date, distance=None):
            #TODO FIX ALL THIS BS
            self.flightID = flightID
            self.date = date
            self.FPD = "https://api.flightplandatabase.com/plans"
            self.AvStack = "http://api.aviationstack.com/v1/flights"
        
            departure_icao, arrival_icao, plane_icao, airline_icao = self.getLocations()
            print("GOT LOCATIONS")
            self.plane = Plane(plane_icao, airline_icao) #TODO FIX THIS
    
            self.start = departure_icao
            self.end = arrival_icao

            print("PRE DISTANCE CHECK")
            if distance is not None:
                self.distance = distance
            else:
                self.distance = self.getDistance()
                
            print(f"POST DISTANCE CHECK: {self.distance}")
            self.fuel = float(self.distance) / float(self.plane.mileage)
            print("CHECK THE MILEAGE")
            self.carbonImpact = self.calcImpact()
            self.impactPerCapita = self.calcImpactPerCapita()

        def fuelPerSeat(self):
            if self.plane.passengers == 0 or None:
                raise Exception("Passengers not set!")
    
            self.fuelPerCapita = self.distance / self.plane.passengers  

        def getLocations(self):
            access_key = os.getenv('AVIATIONSTACK_API_KEY')
    
            queryString = {
                "access_key": access_key,
                #"flight_date": self.date, # ASSUME TODAY ALL THE TIME
                "flight_icao": self.flightID
            }
            response = requests.get("https://api.aviationstack.com/v1/flights", queryString)
    
            if response.status_code != 200:
                print(f"Error fetching flights: {response.status_code}")
                return None, None, None, None, None, None
    
            data = response.json()
            # flight = data['data'][0]
            if not data.get('data') or len(data['data']) == 0:
                raise ValueError(f"No flight data found for flight number {self.flightID} on {self.date}")

            flight = data['data'][0]

            airline_name = flight['airline']['name']
            print(airline_name)
            airline_icao = flight['airline']['icao']
            print(airline_icao)
            flight_icao = flight['flight']['icao']
            print(flight_icao)
            departure_airport = flight['departure']['airport']
            print(departure_airport)
            arrival_airport = flight['arrival']['airport']
            print(arrival_airport)
            departure_icao = flight['departure']['icao']
            print(departure_icao)
            arrival_icao = flight['arrival']['icao']
            print(arrival_icao)

            aircraft_info = flight.get('aircraft')

            if aircraft_info is None:
                print(f"Aircraft data missing for flight {flight.get('flight', {}).get('icao', 'UNKNOWN')}.")

                # Fallback based on airline ICAO
                plane_icao = default_aircraft_by_airline.get(airline_icao, 'A320')

            else:
                plane_icao = aircraft_info.get('icao')
                if plane_icao is None:
                    print(f"Aircraft exists but ICAO missing for flight {flight.get('flight', {}).get('icao', 'UNKNOWN')}.")
                    plane_icao = default_aircraft_by_airline.get(airline_icao, 'A320') 
    
            print(f"{airline_name} flight {flight_icao} from {departure_airport} ({departure_icao}) to {arrival_airport} ({arrival_icao}) uses {plane_icao}")
    
            return departure_icao, arrival_icao, plane_icao, airline_icao
        
        def calcImpact(self):
            if not self.distance or not self.plane or not self.fuel:
                raise Exception("Missing data for carbon impact.\nCheck distance, plane, and fuel")
            
            kgFuel = float(self.fuel) * 3.039 # Gallons to Kilogram
            self.carbonImpact = round(kgFuel * 3.16, 3)
            # print(f"Carbon Impact: {self.carbonImpact}")
            return self.carbonImpact

        def calcImpactPerCapita(self):
            if not self.plane.passengers:
                raise Exception("Passengers not set!")
            
            self.impactPerCapita = round(self.calcImpact() / self.plane.passengers, 3)
            self.impactPerCapita = self.carbonImpact / float(self.plane.passengers)
            print(f"Carbon Impact Per Capita: {self.impactPerCapita}")
            return self.impactPerCapita

        def getDistance(self):
            access_key = os.getenv('FDP_API_KEY')
            url = "https://api.flightplandatabase.com/auto/generate"
            payload = {"fromICAO":self.start, "toICAO":self.end}

            headers = {
            # "Authorization": f"Bearer {access_key}"
            #"X-Units": "AVIATION"  # Optional: "nm" for nautical miles, "km" for kilometers, "mi" for miles
            }

            response = requests.post(
                url,
                json=payload,
                headers=headers,
                auth=(access_key, '')
            )

            data = response.json()
            # if "error" in data:
            #     print(f"API error: {data['error']}")
            #     return None
            
            distance = (data.get('distance'))



            # if distance is not None:
            #     print(f"Flight from {self.start} to {self.end} is approximately {distance} nautical miles.")
            # else:
            #     print(f"No distance found in response for {self.start} to {self.end}")

            return distance
        

        def getAirline(self):
            airlineTag = ''.join(c for c in self.flightID if c.isalpha())
            return airlineTag
