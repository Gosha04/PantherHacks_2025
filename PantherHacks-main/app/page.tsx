"use client"

import Image from "next/image";
import * as React from "react"
import { useRouter } from 'next/navigation';
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

import { format } from "date-fns"
import { CalendarIcon } from "lucide-react"
 
import { cn } from "@/lib/utils"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
import Footer from '@/components/ui/Footer';

export default function Home() {
  const [date, setDate] = React.useState<Date>()
  const [flightNumber, setFlightNumber] = React.useState(""); // Add state for flight number
  const router = useRouter();

  const handleSearch = () => {
    const formattedDate = date ? format(date, "yyyy-MM-dd") : "";
    // Navigate to the results page with query parameters
    router.push(`/results?flight=${flightNumber}&date=${formattedDate}`);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 pb-20 gap-8 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[10px] items-center sm:items-start">
      <div className="p-10">
        <Image
        src="/top-logo.svg"
        width={500}
        height={500}
        alt="Fly Conscious"
        />
      </div>
        <Card className="w-[600px]">
        <CardHeader>
          <CardTitle>Find your flight!</CardTitle>
          <CardDescription>Search for a flight to get CO2 emission data.</CardDescription>
        </CardHeader>
        <CardContent>
          <form>
            <div className="grid w-full items-center gap-4">
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="flight number">Flight Number</Label>
                {/* Bind input value to state and add onChange handler */}
                <Input
                  id="flight"
                  placeholder="Enter your flight number"
                  value={flightNumber}
                  onChange={(e) => setFlightNumber(e.target.value)}
                 />
              </div>
            </div>
            <div className="grid w-full items-center gap-4 mt-5">
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="date">Date</Label>
                <Popover>
                  <PopoverTrigger asChild>
                    <Button
                    variant={"outline"}
                    className={cn(
                    "w-[240px] justify-start text-left font-normal",
                    !date && "text-muted-foreground"
                    )}
                  >
                    <CalendarIcon />
                    {date ? format(date, "PPP") : <span>Select a date</span>}
                  </Button>
                </PopoverTrigger>
                <PopoverContent className="w-auto p-0" align="start">
                <Calendar
                  mode="single"
                  selected={date}
                  onSelect={setDate}
                  initialFocus
                />
                </PopoverContent>
              </Popover>
              </div>
            </div>
          </form>
        </CardContent>
        <CardFooter className="flex justify-between">
          <Button onClick={handleSearch} disabled={!flightNumber || !date}>Search</Button>
        </CardFooter>
      </Card>
      </main>
      <Footer></Footer>
    </div>
  );
}
