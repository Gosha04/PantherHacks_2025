-- MySQL dump 10.13  Distrib 9.2.0, for macos14.7 (x86_64)
--
-- Host: 127.0.0.1    Database: Flight_Tracker
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport` (
  `ID` int NOT NULL,
  `CountryID` int DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Name` (`Name`),
  KEY `CountryID` (`CountryID`),
  CONSTRAINT `airport_ibfk_1` FOREIGN KEY (`CountryID`) REFERENCES `country` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `ID` int NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `ID` int NOT NULL,
  `StartID` int DEFAULT NULL,
  `EndID` int DEFAULT NULL,
  `Airline` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Airline` (`Airline`),
  KEY `StartID` (`StartID`),
  KEY `EndID` (`EndID`),
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`StartID`) REFERENCES `airport` (`ID`),
  CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`EndID`) REFERENCES `airport` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plane`
--

DROP TABLE IF EXISTS `plane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plane` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Mileage` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plane`
--

LOCK TABLES `plane` WRITE;
/*!40000 ALTER TABLE `plane` DISABLE KEYS */;
INSERT INTO `plane` VALUES ('A109','SABCA A-109',NULL),('A119','DENEL Koala',NULL),('A139','BELL-AGUSTA AB-139',NULL),('A148','Antonov An-148',NULL),('A19N','Airbus A319neo',NULL),('A20N','Airbus A320neo',NULL),('A21N','Airbus A321neo',NULL),('A306','Airbus A300F4-600',NULL),('A310','Airbus A310',NULL),('A319','Airbus A319',NULL),('A320','Airbus A320',NULL),('A321','Airbus A321',NULL),('A330','Airbus A330',NULL),('A332','Airbus A330-200',NULL),('A333','Airbus A330-300',NULL),('A338','Airbus A330-800',NULL),('A339','Airbus A330-900',NULL),('A343','Airbus A340-300',NULL),('A346','Airbus A340-600',NULL),('A359','Airbus A350-900',NULL),('A35K','Airbus A350-1000',NULL),('A388','Airbus A380-800',NULL),('A400','AIRBUS A-400M Atlas',NULL),('AA1','Grumman Tr2',NULL),('AA5','Grumman AA-5 Tiger',NULL),('AC11','Rockwell Commander 114',NULL),('AC50','Aero Commander 500',NULL),('AC6L','Rockwell Commander 685',NULL),('AC90','Rockwell Turbo Commander 690',NULL),('AJ27','COMAC ARJ-21-700 Xiangfeng',NULL),('AN12','Antonov An-12',NULL),('AS50','Eurocopter AS-350 AStar',NULL),('ASTO','TECNAM Astore',NULL),('AT43','Aerospatiale ATR-42-300',NULL),('AT46','Aerospatiale ATR-42-600',NULL),('AT5T','AIR TRACTOR AT-503',NULL),('AT6T','AIR TRACTOR AT-602',NULL),('AT72','ATR ATR-72',NULL),('AT75','Aerospatiale ATR-72-500',NULL),('AT76','Aerospatiale ATR-72-600',NULL),('AT8T','Air Tractor AT-802',NULL),('B06','Bell JetRanger',NULL),('B190','Beechcraft 1900',NULL),('B350','Beechcraft Super King Air 350',NULL),('B38M','Boeing 737 MAX 8',NULL),('B39M','Boeing 737 MAX 9',NULL),('B407','Bell 407',NULL),('B412','Bell 412',NULL),('B429','Bell 429 GlobalRanger',NULL),('B505','Bell 505',NULL),('B58T','BEECH 58P Pressurized Baron',NULL),('B712','Boeing 717-200',NULL),('B722','BOEING 727-200',NULL),('B732','Boeing 737-200',NULL),('B733','BOEING 737-300',NULL),('B734','BOEING 737-400',NULL),('B735','Boeing 737-500',NULL),('B736','BOEING 737-600',NULL),('B737','Boeing 737-700',NULL),('B738','Boeing 737-800',NULL),('B739','Boeing 737-900',NULL),('B744','Boeing 747-400',NULL),('B748','BOEING 747-8',NULL),('B752','Boeing 757-200',NULL),('B753','BOEING 757-300',NULL),('B762','BOEING 767-200',NULL),('B763','BOEING 767-300',NULL),('B764','BOEING 767-400',NULL),('B772','Boeing 777-200',NULL),('B773','BOEING 777-300',NULL),('B77L','BOEING 777-200LR',NULL),('B77W','BOEING 777-300ER',NULL),('B787','Boeing 787-8',NULL),('B789','Boeing 787-9 Dreamliner',NULL),('B78X','BOEING 787-10 Dreamliner',NULL),('BCS1','Airbus A220-100',NULL),('BCS3','Airbus A220-300',NULL),('BE10','Beechcraft King Air 100',NULL),('BE18','Beechcraft 18',NULL),('BE20','Beechcraft Super King Air 200',NULL),('BE23','Beechcraft Sundowner',NULL),('BE33','Beechcraft Bonanza (33)',NULL),('BE35','Beechcraft 35 Bonanza',NULL),('BE36','Beechcraft Bonanza (36)',NULL),('BE40','Beechcraft Beechjet',NULL),('BE50','Beechcraft Twin Bonanza',NULL),('BE55','Beechcraft 55 Baron',NULL),('BE58','Beechcraft Baron (58)',NULL),('BE65','Beechcraft Queen Air (65)',NULL),('BE95','Beechcraft Travel Air',NULL),('BE99','Beechcraft Airliner',NULL),('BE9L','Beechcraft King Air 90',NULL),('BL17','BELLANCA Viking',NULL),('BL8','CHAMPION Decathlon',NULL),('BT36','Beechcraft Bonanza (36) Turbo',NULL),('C140','Cessna 140',NULL),('C150','Cessna Commuter',NULL),('C152','Cessna 152',NULL),('C162','Cessna Skycatcher',NULL),('C172','Cessna Skyhawk',NULL),('C175','Cessna 175 Skylark',NULL),('C177','Cessna Cardinal',NULL),('C180','Cessna Skywagon 180',NULL),('C182','Cessna Skylane',NULL),('C185','Cessna Skywagon',NULL),('C205','Cessna 205',NULL),('C206','Cessna 206 Stationair',NULL),('C207','Cessna T207 Turbo Stationair 8',NULL),('C208','Cessna Caravan',NULL),('C210','Cessna Centurion',NULL),('C25A','Cessna Citation CJ2+',NULL),('C25B','Cessna Citation CJ3',NULL),('C25C','Cessna Citation CJ4',NULL),('C25M','Cessna Citation M2',NULL),('C30J','Lockheed EC-130J Hercules',NULL),('C310','Cessna 310',NULL),('C337','Cessna Super Skymaster',NULL),('C340','Cessna 340',NULL),('C402','Cessna 402',NULL),('C404','Cessna 404 Titan',NULL),('C408','CESSNA 408 SkyCourier',NULL),('C414','Cessna Chancellor',NULL),('C421','Cessna 421',NULL),('C425','Cessna Conquest 1',NULL),('C441','Cessna Conquest 2',NULL),('C510','Cessna Citation Mustang',NULL),('C525','Cessna Citation CJ1',NULL),('C550','Cessna Citation II',NULL),('C560','Cessna Citation V',NULL),('C56X','Cessna Citation Excel/XLS',NULL),('C650','Cessna Citation III',NULL),('C680','Cessna Citation Sovereign',NULL),('C68A','Cessna Citation Latitude',NULL),('C700','Cessna Citation Longitude',NULL),('C72R','Cessna Cutlass RG',NULL),('C750','Cessna Citation X',NULL),('C82R','Cessna Skylane RG',NULL),('C82S','CESSNA T182 Turbo Skylane',NULL),('C82T','CESSNA Turbo Skylane RG',NULL),('C919','COMAC C-919',NULL),('CH7B','CHAMPION Sky-Trac',NULL),('CL30','Bombardier Challenger 300',NULL),('CL35','Canadair Challenger 350',NULL),('CL60','Canadair Challenger',NULL),('CRJ2','Canadair Regional Jet CRJ-200',NULL),('CRJ7','Canadair Regional Jet CRJ-700',NULL),('CRJ9','Canadair Regional Jet CRJ-900',NULL),('CVLT','CONVAIR CV-580',NULL),('D328','Fairchild Dornier 328',NULL),('DA40','Diamond Star',NULL),('DA42','Diamond Twin Star',NULL),('DA62','Diamond DA-62',NULL),('DC3','Douglas DC-3',NULL),('DH8A','de Havilland Dash 8-100',NULL),('DH8B','de Havilland Dash 8-200',NULL),('DH8C','de Havilland Dash 8-300',NULL),('DH8D','de Havilland Dash 8-400',NULL),('DHC6','De Havilland Canada Twin Otter',NULL),('DV20','Diamond DV-20 Katana',NULL),('E120','Embraer EMB-120 Brasilia',NULL),('E135','Embraer ERJ-135',NULL),('E145','Embraer ERJ-145',NULL),('E170','Embraer 170/175',NULL),('E190','Embraer ERJ-190',NULL),('E290','Embraer E190-E2',NULL),('E295','EMBRAER ERJ-190-400',NULL),('E35L','Embraer Legacy 600/650',NULL),('E50P','Embraer Phenom 100',NULL),('E545','Embraer Legacy 450',NULL),('E550','Embraer Legacy 550',NULL),('E55P','Embraer Phenom 300',NULL),('E75L','EMBRAER 175 (long wing)',NULL),('E75S','Embraer ERJ 175',NULL),('EA50','Eclipse 500',NULL),('EC20','Eurocopter EC-120 Colibri',NULL),('EC30','Eurocopter EC-130',NULL),('EC35','Eurocopter EC-635',NULL),('EC45','KAWASAKI EC-145',NULL),('ECHO','TECNAM SeaSky',NULL),('EPIC','Epic Aircraft LT',NULL),('ERCO','ERCO Ercoupe',NULL),('F100','Fokker 100',NULL),('F2TH','Dassault Falcon 2000',NULL),('F50','Fokker Maritime Enforcer',NULL),('F900','Dassault Falcon 900',NULL),('FA20','Dassault Falcon 20',NULL),('FA50','Dassault Falcon 50',NULL),('FA7X','Dassault Falcon 7X',NULL),('FA8X','Dassault Falcon 8X',NULL),('FU24','SARGENT-FLETCHER FU-24',NULL),('G150','IAI Gulfstream G150',NULL),('G280','IAI Gulfstream G280',NULL),('GA7C','GULFSTREAM AEROSPACE G-8 Gulfstream G700',NULL),('GA8','GIPPSLAND GA-8 Airvan',NULL),('GALX','IAI Gulfstream G200',NULL),('GL5T','Bombardier Global 5000',NULL),('GL7T','BOMBARDIER BD-700 Global 7500',NULL),('GLAS','STODDARD-HAMILTON Glasair',NULL),('GLEX','Bombardier Global Express',NULL),('GLF3','Gulfstream Aerospace Gulfstream 3',NULL),('GLF4','Gulfstream Aerospace Gulfstream IV',NULL),('GLF5','Gulfstream Aerospace Gulfstream V',NULL),('GLF6','Gulfstream Aerospace Gulfstream G650',NULL),('H25B','Hawker 800',NULL),('H500','MD Helicopters MD 500',NULL),('HA4T','Hawker Beechcraft 4000',NULL),('HUSK','CHRISTEN Husky',NULL),('KODI','Quest Kodiak',NULL),('LJ31','Learjet 31',NULL),('LJ35','Learjet 35',NULL),('LJ40','Learjet 40',NULL),('LJ45','Learjet 45',NULL),('LJ55','Learjet 55',NULL),('LJ60','Learjet 60',NULL),('LJ75','Bombardier Learjet 75',NULL),('M20P','Mooney M-20',NULL),('M20T','Mooney M-20 Turbo',NULL),('M7','MAULE MT-7-260 Super Rocket',NULL),('MD11','Boeing MD-11',NULL),('MD82','McDonnell Douglas MD-82',NULL),('P06T','TECNAM P-2006T',NULL),('P180','Piaggio P.180 Avanti',NULL),('P208','TECNAM P-2008',NULL),('P210','Cessna P210 Pressurized Centurion',NULL),('P212','TECNAM P-2012 Traveller',NULL),('P28A','Piper Cherokee',NULL),('P28B','Piper Dakota / Pathfinder',NULL),('P28R','Piper Cherokee Arrow',NULL),('P28T','Piper Arrow 4',NULL),('P32R','Piper Saratoga/Lance',NULL),('P32T','Piper Lance 2',NULL),('P337','Cessna T337G Pressurized Skymaster',NULL),('P46T','Piper Malibu Meridian',NULL),('PA16','Piper PA-16 Clipper',NULL),('PA18','Piper L-21 Super Cub',NULL),('PA22','Piper PA-22 Tri-Pacer',NULL),('PA23','Piper Apache',NULL),('PA24','Piper PA-24 Comanche',NULL),('PA27','Piper Aztec',NULL),('PA30','Piper PA-30 Twin Comanche',NULL),('PA31','Piper Navajo',NULL),('PA32','Piper Saratoga',NULL),('PA34','Piper Seneca',NULL),('PA38','Piper Tomahawk',NULL),('PA44','Piper PA-44 Seminole',NULL),('PA46','Piper Malibu Mirage',NULL),('PAT4','Piper PA-31T3-500 T-1040',NULL),('PAY3','Piper Cheyenne 3',NULL),('PAY4','Piper Cheyenne 400',NULL),('PC12','Pilatus PC-12',NULL),('R22','Robinson R-22',NULL),('R44','Robinson R-44',NULL),('R66','Robinson R-66',NULL),('RV12','Van\'s RV-12',NULL),('RV9','Van\'s RV-9',NULL),('S22T','Cirrus SR22 Turbo',NULL),('S92','Sikorsky Helibus',NULL),('SF34','Saab 340',NULL),('SF50','Cirrus Vision SF50',NULL),('SIRA','TECNAM Sierra',NULL),('SR20','Cirrus SR-20',NULL),('SR22','Cirrus SR-22',NULL),('SU95','Sukhoi Superjet 100',NULL),('SW4','Fairchild Dornier SA-227DC Metro',NULL),('T18','THORP Tiger',NULL),('T204','Tupolev Tu-214',NULL),('T206','Cessna T206 Turbo Stationair',NULL),('T210','Cessna T210 Turbo Centurion',NULL),('T34P','Beechcraft Mentor',NULL),('T6','North American T-6 Texan',NULL),('TBM7','Socata TBM-700',NULL),('TBM9','Daher-Socata TBM-900',NULL),('TWEN','TECNAM P-2010 Twenty-Ten',NULL),('UH1','Bell UH-1V Iroquois',NULL),('YK52','YAKOVLEV Yak-52',NULL);
/*!40000 ALTER TABLE `plane` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-25 18:35:18
