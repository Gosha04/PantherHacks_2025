import React from 'react';
import Image from "next/image";
import { Card, CardContent } from "@/components/ui/card";

interface FlightDetailsCardProps {
  flightNum: string;
  planeModel: string;
  airline: string;
  passengers: string;
  distance: string;
}

const FlightDetailsCard: React.FC<FlightDetailsCardProps> = ({
  flightNum,
  planeModel,
  airline,
  passengers,
  distance,
}) => {
  return (
    <div className="p-1">
      <Card>
        <CardContent className="flex flex-col gap-8 items-center justify-center px-10 py-5">
          <div className="text-center">
            <h2 className="text-2xl font-semibold">Your flight: {flightNum}</h2>
        </div>
          <div className="flex flex-row gap-20">
            <div className="flex flex-col gap-1 items-center justify-center">
              <div className="text-center">
                <Image
            src="/plane.svg"
            width={55}
            height={55}
            alt="Airplane"
            style={{ opacity: 0.75 }}
                />
              </div>
              <h3 className="text-md font-medium">{planeModel}</h3>
            </div>
            <div className="flex flex-col gap-1 items-center justify-center">
              <div className="text-center">
                <Image
            src="/airline.svg"
            width={55}
            height={55}
            alt="Airline"
            style={{ opacity: 0.75 }}
                />
              </div>
              <h3 className="text-md font-medium">{airline}</h3>
            </div>
            <div className="flex flex-col gap-1 items-center justify-center">
              <div className="text-center">
                <Image
            src="/passengers.svg"
            width={55}
            height={55}
            alt="Passengers"
            style={{ opacity: 0.75 }}
                />
              </div>
              <h3 className="text-md font-medium">{passengers} Passengers</h3>
            </div>
            <div className="flex flex-col gap-1 items-center justify-center">
              <div className="text-center">
                <Image
            src="/milage.svg"
            width={55}
            height={55}
            alt="Mileage"
            style={{ opacity: 0.75 }}
                />
              </div>
              <h3 className="text-md font-medium">{distance} Miles</h3>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default FlightDetailsCard;