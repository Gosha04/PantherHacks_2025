import mysql.connector
import os
from dotenv import load_dotenv
import requests
import json
import csv


script_dir = os.path.dirname(os.path.abspath(__file__))
plane_data_path = os.path.join(script_dir, "plane_data.json")
with open(plane_data_path, "r") as f:
    plane_data = json.load(f)

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

# def openJSON(filename):
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     return data

def openJSON(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def csvToJSON(name):
    data = []
    csvName = name+'.csv'
    jsonName = name+'.json'
    with open(csvName, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Each row becomes a dictionary
        for row in reader:
            data.append(row)
    
    with open(jsonName, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

#csvToJSON("plane_data")   
planeInfo = openJSON('plane_data.json') 
loadFactor = openJSON('loadFactorICAO.json')

class Plane:
    def __init__(self, code, airline):
        if code is None:
            raise ValueError("Plane ICAO code cannot be None")
        self.code = code
        self.model = self.getModel() # icao
        self.seats = self.getSeats()

        if self.seats is str:
            self.seats = 0
        
        self.airline = airline
        self.passengers = float(self.seats) * 0.78
        if airline in loadFactor:
            self.passengers = self.seats * float(loadFactor[airline])
            # print("Passengers were checked")
        # self.mileage = self.getMileage # mpg
        self.mileage = self.getMileage()

        # mycursor.execute("""INSERT INTO plane VALUES (%s, %s, %s, %s, %s)""", (self.code, self.seats, self.airline, self.passengers, self.mileage))
        # mydb.commit()
        mycursor.execute("SELECT * FROM plane WHERE code = %s", (self.code,))
        result = mycursor.fetchone()

        if result is None:
            mycursor.execute("""INSERT INTO plane (code, seats, airline, passengers, mileage)
                        VALUES (%s, %s, %s, %s, %s)""",
                        (self.code, self.seats, self.airline, self.passengers, self.mileage))
            mydb.commit()
        # else:
        #     print(f"Plane {self.code} already exists in database.")

    
    def getMileage(self):
         for plane in planeInfo:
             if self.code == plane['icao_code']:
                #  print(plane['mpg'])
                 return plane['mpg']
    
    def getSeats(self):
        for plane in planeInfo:
            if self.code == plane['icao_code']:
            #    print(plane['maxSeats'])
               return plane['maxSeats']

    def getModel(self):
        for plane in planeInfo:
            if self.code == plane['icao_code']:
            #    print(plane['model_name'])
               return plane['model_name']
            
    def getMileage(self):
        for plane in planeInfo:
            if self.code == plane['icao_code']:
                print(plane['mpg'])
                return plane['mpg']