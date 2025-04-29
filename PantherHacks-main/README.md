# PantherHacks

## **Fork Note
  While this project was forked from our Hackathon repository due to a security issue, credit goes to all 4 members listed in Contributors.

## **Flight Conscious**
  Flight Conscious is a sustainable aviation web application that calculates the carbon emissions of your flights and recommends more enviromentally friendly flight alternatives.

## **Description**
  Flight Conscious helps travelers understand the environmental impact of their air travel by:

  1. Calculating CO₂ emissions based on flight distance, aircaft type, and fuel ussage

## **Features**
  Flight Emissions Calculator
  - Real-time estimation of carbon emissions based on flight data and aircraft fuel efficiency

  Per-Passenger Emission Analysis
  - Calculates emissions based on real passenger occupancy 

  Alternative Flight Suggestions
  - Greener options between the same departure and arrival airports

  Live Flight Data Fetching
  - Integrates with AviationStack and Flight Plan Database APIs

## **Tech Stack**
  Frontend:
  - Next.js/React
  - Tailwindcss

  Backend:
  - Python

  Database:
  - MySQL
  - Dotenv

  External APIs:
  - AviationStack API
  - Flight Plan Database API

## **Setup Instructions**
  APIs
  - Get a free API keys from AviationStack and Flight Plan Database (in .env and replace keys with your own personal keys!)

  Backend  
  Install MySQL 
  - keep track of your root log in password! (in .env switch mysql_password to your personal password)

  Install mysql.connector and dotenv

  Frontend  
  Install Node.js and React
  - node 
  - npm
  - npx 


## **Usage Example**
  User Input:
  - Enter a Flight ID and Date of Flight

  App Fetches:
  - Departure and arrival airports
  - Aircraft model
  - Estimated distance

  Calculations
  - Total Carbon Emissions
  - Per-passenger Emissions

## **Aspirations**
  1. Providing alternative flight options to reduce carbon footprint

## **Contributors**
  1. Josh Vaysman
  2. Noslen Cruz-Muniz
  3. Divi Newton
  4. Julia Nguyen
