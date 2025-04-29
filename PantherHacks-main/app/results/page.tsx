"use client";

// Import useEffect and useSearchParams
import React, { useState, useEffect } from 'react';
import Image from "next/image";
import Link from 'next/link';
import SimilarFlightCard from '@/components/ui/SimilarFlightCard';
import Footer from '@/components/ui/Footer';
import EmissionStatsCard from '@/components/ui/EmissionStatsCard';
import FlightDetailsCard from '@/components/ui/FlightDetailsCard';
import { Button } from '@/components/ui/button';
import { useSearchParams } from 'next/navigation';

export default function Results() {
    const [flightData, setFlightData] = useState<any>(null); // State to hold the API response
    const [error, setError] = useState<string | null>(null); // State for error messages
    const [showSimilarFlights, setShowSimilarFlights] = useState(false);
    const [isLoading, setIsLoading] = useState(true); // Add loading state

    // ... state variables for displaying flight details remain the same ...
    const [originCode, setOriginCode] = useState("");
    const [destinationCode, setDestinationCode] = useState("");
    const [originFull, setOriginFull] = useState("");
    const [destinationFull, setDestinationFull] = useState("");
    const [displayDate, setDisplayDate] = useState(""); // Separate state for displaying date
    const [displayFlightNum, setDisplayFlightNum] = useState(""); // Separate state for displaying flight number
    const [plane, setPlane] = useState("");
    const [airline, setAirline] = useState("");
    const [pplCount, setPplCount] = useState("");
    const [distance, setDistance] = useState("");
    const [netCo2, setNetCo2] = useState("");
    const [singleCo2, setSingleCo2] = useState("");

    // Similar flights state
    const [similarFlights, setSimilarFlights] = useState<
      { carbonReduction: string | null, planeModel: string | null, flightNum: string | null, emissionsPerPerson: string | null }[]
    >([
      { carbonReduction: null, planeModel: null, flightNum: null, emissionsPerPerson: null },
      { carbonReduction: null, planeModel: null, flightNum: null, emissionsPerPerson: null },
      { carbonReduction: null, planeModel: null, flightNum: null, emissionsPerPerson: null },
      { carbonReduction: null, planeModel: null, flightNum: null, emissionsPerPerson: null },
    ]);

    // Get search params from URL
    const searchParams = useSearchParams();

    // Rename handleSubmit to fetchFlightData and accept parameters
    const fetchFlightData = async (flightNumParam: string, dateParam: string) => {
        setIsLoading(true); // Start loading
        setFlightData(null); // Reset previous data
        setError(null); // Reset previous error
        // ... reset individual states ...
        setOriginCode("");
        setDestinationCode("");
        setOriginFull("");
        setDestinationFull("");
        setDisplayDate("");
        setDisplayFlightNum("");
        setPlane("");
        setAirline("");
        setPplCount("");
        setDistance("");
        setNetCo2("");
        setSingleCo2("");
        setShowSimilarFlights(false); // Reset similar flights view

        // Basic validation
        if (!flightNumParam || !dateParam) {
            setError("Flight number and date are required.");
            setIsLoading(false);
            return;
        }

        try {
          const res = await fetch("/api/run-python", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            // Use parameters passed to the function
            body: JSON.stringify({ flight_number: flightNumParam, date: dateParam }),
          });
          if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
          }
          const data = await res.json();
          if (data.error) {
            setError(data.error);
          } else {
            setFlightData(data); // Store the entire response object

            // ... set individual state variables from the response data ...
            setOriginCode(data.origin_code || "");
            setDestinationCode(data.destination_code || "");
            setOriginFull(data.origin_full || "");
            setDestinationFull(data.destination_full || "");
            setDisplayDate(data.date || "");
            setDisplayFlightNum(data.flight_num || "");
            setPlane(data.plane || "");
            setAirline(data.airline || "");
            setPplCount(String(data.ppl_count || ""));
            setDistance(String(data.distance || ""));
            setNetCo2(String(data.net_co2 || ""));
            setSingleCo2(String(data.single_co2 || ""));
            setSimilarFlights(
              Array.isArray(data.similar_flights)
                ? data.similar_flights
                : [
                    { carbonReduction: null, planeModel: null, flightNum: null, emissionsPerPerson: null },
                    { carbonReduction: null, planeModel: null, flightNum: null, emissionsPerPerson: null },
                    { carbonReduction: null, planeModel: null, flightNum: null, emissionsPerPerson: null },
                    { carbonReduction: null, planeModel: null, flightNum: null, emissionsPerPerson: null },
                  ]
            );
          }
        } catch (e: any) {
          console.error("Fetch error:", e);
          setError(`Failed to fetch flight data: ${e.message}`);
          setFlightData(null);
        } finally {
            setIsLoading(false); // Stop loading regardless of outcome
        }
      };

    // Use useEffect to fetch data when component mounts or params change
    useEffect(() => {
        const flightNum = searchParams.get('flight');
        const flightDate = searchParams.get('date');

        if (flightNum && flightDate) {
            fetchFlightData(flightNum, flightDate);
        } else {
            // Handle cases where parameters are missing
            setError("Flight number or date missing in URL.");
            setIsLoading(false);
        }
        // Dependency array includes searchParams to refetch if URL changes
    }, [searchParams]);

  return (
    <>
    {/* Added relative positioning */}
    <div className="flex flex-col items-center justify-center min-h-screen p-8 pb-20 gap-8 sm:p-20 font-[family-name:var(--font-geist-sans)] relative">
      {/* Navbar - Remove input fields and button */}
      <nav className="fixed top-0 left-0 right-0 flex gap-10 items-center justify-between p-1 px-8 border shadow-sm bg-card text-card-foreground z-50 backdrop-blur-sm">
        <div>
        <Link href="/">
        <div className="p-10">
          <Image
          src="/top-logo.svg"
          width={200}
          height={200}
          alt="Fly Conscious"
          />
        </div>
        </Link>
        </div>
        {/* Removed input fields and submit button */}
         {/* Add a link back to search or modify search */}
         <div>
            <Link href="/">
                <Button variant="outline" className="px-4 py-2">
                    New Search
                </Button>
            </Link>
        </div>
      </nav>

      {/* Add Loading Indicator */}
      {isLoading && <p className="pt-20 text-lg">Loading flight data...</p>}

      {/* Keep error display */}
      {error && !isLoading && <h2 className="pt-20 text-lg" style={{ color: "red" }}>Error: {error}</h2>}

      {/* Display results only when not loading and no error */}
      {!isLoading && !error && flightData && (
        <>
        {/* Results grid */}
        <div className="grid grid-cols-3 gap-2 items-center justify-center mx-auto pt-20"> {/* Adjusted padding-top */}
        {/* ... rest of the results display code remains the same ... */}
        <div className="text-center">
          <h2 className="text-5xl font-semibold">{originCode}</h2>
          <p>{originFull}</p>
        </div>
        <div className="text-center">
          <Image
            src="/planearrow.svg"
            width={200}
            height={200}
            alt="to"
          />
        </div>
        <div className="text-center">
          <h2 className="text-5xl font-semibold">{destinationCode}</h2>
          <p>{destinationFull}</p>
        </div>
      </div>
      <div className="text-center">
        <h2 className="text-2xl font-semibold">{displayDate}</h2>
      </div>
      <FlightDetailsCard
        flightNum={displayFlightNum}
        planeModel={plane}
        airline={airline}
        passengers={pplCount}
        distance={distance}
      />
      <EmissionStatsCard
        netEmissions={netCo2}
        emissionsPerPerson={singleCo2}
      />
      <div className="flex flex-col gap-3 text-center mt-8">
          <h2 className="text-2xl font-semibold">Improve your Carbon Emissions</h2>
            <p className="max-w-[80%] mx-auto">You can lower your carbon footprint by switching to a more efficient flight on the same day. We've found a list of alternative flights that combine more passengers to reduce emissions. Consider booking one of these options to make a positive impact!</p>
        </div>
        {/* Show Flights Button */}
        {!showSimilarFlights && (
            <Button onClick={() => setShowSimilarFlights(true)} className="mt-0">
              Show Flights
            </Button>
          )}
        </>
      )}

      {/* Similar Flights Section (only shown if data exists and button clicked) */}
      {!isLoading && !error && flightData && showSimilarFlights && (
        <>
          <div className="text-center pt-10">
            <h2 className="text-2xl font-semibold">Consolidated Flights List</h2>
          </div>
          {similarFlights.map((flight, idx) => (
            <SimilarFlightCard
              key={idx}
              carbonReduction={flight.carbonReduction ?? ""}
              planeModel={flight.planeModel ?? ""}
              flightNum={flight.flightNum ?? ""}
              emissionsPerPerson={flight.emissionsPerPerson ?? ""}
            />
          ))}
        </>
      )}

      <Footer></Footer>
    </div>
    </>
  );
}