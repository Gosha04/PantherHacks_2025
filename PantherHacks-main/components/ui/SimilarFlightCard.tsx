import React from 'react';
import Image from 'next/image';
import { Card, CardContent } from '@/components/ui/card';

interface SimilarFlightCardProps {
  flightNum: string;
  carbonReduction: string;
  planeModel: string;
  emissionsPerPerson: string;
}

const SimilarFlightCard: React.FC<SimilarFlightCardProps> = ({
  flightNum,
  carbonReduction,
  planeModel,
  emissionsPerPerson,
}) => {
  return (
    <div className="p-1">
      <Card>
        <CardContent className="flex flex-row gap-4 items-center justify-between p-6 w-225 h-10">
          <div className="flex flex-row gap-1 items-center justify-center">
            <div className="text-center">
              <Image
                src="/airline.svg"
                width={25}
                height={25}
                alt="airline"
                style={{ opacity: 0.75 }}
              />
            </div>
            <h3 className="text-md font-medium">{flightNum}</h3>
          </div>
          <div className="flex flex-row gap-1 items-center justify-center">
            <div className="text-center">
              <Image
                src="/co2.svg"
                width={35}
                height={35}
                alt="CO2"
                style={{ opacity: 0.75 }}
              />
            </div>
            <h3 className="text-md font-medium">{carbonReduction} Carbon</h3>
          </div>
          <div className="flex flex-row gap-1 items-center justify-center">
            <div className="text-center">
              <Image
                src="/plane.svg"
                width={25}
                height={25}
                alt="Airplane"
                style={{ opacity: 0.75 }}
              />
            </div>
            <h3 className="text-md font-medium">{planeModel}</h3>
          </div>
          <div className="flex flex-row gap-1 items-center justify-center">
            <div className="text-center">
              <Image
                src="/passengers.svg"
                width={25}
                height={25}
                alt="Per Person Emissions"
                style={{ opacity: 0.75 }}
              />
            </div>
            <h3 className="text-md font-medium">{emissionsPerPerson} Per Person</h3>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default SimilarFlightCard;