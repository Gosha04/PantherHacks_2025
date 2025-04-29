import React from 'react';
import { Card, CardContent } from "@/components/ui/card";

interface EmissionStatsCardProps {
  netEmissions: string;
  emissionsPerPerson: string;
}

const EmissionStatsCard: React.FC<EmissionStatsCardProps> = ({ netEmissions, emissionsPerPerson }) => {
  return (
    <div className="flex justify-center gap-4">
      <div className="p-1">
        <Card>
          <CardContent className="flex flex-col gap-4 items-center justify-center p-10">
            <h3 className="text-md font-medium">Net Carbon Emissions</h3>
            <h1 className="text-5xl">{netEmissions} t</h1>
          </CardContent>
        </Card>
      </div>
      <div className="p-1">
        <Card>
          <CardContent className="flex flex-col gap-4 items-center justify-center p-10">
            <h3 className="text-md font-medium">Emissions Per Person</h3>
            <h1 className="text-5xl">{emissionsPerPerson} t</h1>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default EmissionStatsCard;