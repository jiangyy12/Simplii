-- MySQL dump 10.13  Distrib 8.0.26, for macos11 (x86_64)
--
-- Host: 127.0.0.1    Database: tasks
-- ------------------------------------------------------
-- Server version 8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Categories`
--

DROP TABLE IF EXISTS `Categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Categories` (
  `Category_ID` int NOT NULL,
  `Category_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Category_ID`),
  UNIQUE KEY `Category_name_UNIQUE` (`Category_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categories`
--

LOCK TABLES `Categories` WRITE;
/*!40000 ALTER TABLE `Categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `Categories` ENABLE KEYS */;
UNLOCK TABLES;

BEGIN;
INSERT INTO `Categories` VALUES (1, 'intern');
INSERT INTO `Categories` VALUES (2, 'school');
COMMIT;

--
-- Table structure for table `Login_info`
--

DROP TABLE IF EXISTS `Login_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Login_info` (
  `Login_ID` int NOT NULL,
  `User_ID` int DEFAULT NULL,
  `Password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Login_ID`),
  KEY `UserID_idx` (`User_ID`),
  CONSTRAINT `UserID` FOREIGN KEY (`User_ID`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Login_info`
--

LOCK TABLES `Login_info` WRITE;
/*!40000 ALTER TABLE `Login_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `Login_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tasks`
--

DROP TABLE IF EXISTS `Tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tasks` (
  `TaskID` varchar(45) NOT NULL,
  `UserID` int DEFAULT NULL,
  `Taskname` varchar(45) NOT NULL,
  `Status` varchar(45) DEFAULT NULL,
  `Startdate` datetime DEFAULT NULL,
  `Duedate` datetime DEFAULT NULL,
  `Hours` int DEFAULT NULL,
  `Category` int DEFAULT NULL,
  `Description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`TaskID`),
  UNIQUE KEY `TaskID_UNIQUE` (`TaskID`),
  KEY `UserID_idx` (`UserID`),
  KEY `Category_ID_idx` (`Category`),
  CONSTRAINT `Category_ID` FOREIGN KEY (`Category`) REFERENCES `Categories` (`Category_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `User_ID` FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tasks`
--
BEGIN;
INSERT INTO `Tasks` VALUES (1, 1, 'Create Database', 'In Progress', '2021-11-17 00:00:00', '2021-11-30 23:59:59', 20, 1, 'Create mysql database');
COMMIT;

LOCK TABLES `Tasks` WRITE;
/*!40000 ALTER TABLE `Tasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `UserID` int NOT NULL,
  `EmailID` varchar(45) DEFAULT NULL,
  `FullName` varchar(45) DEFAULT NULL,
  `Password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `EmailID_UNIQUE` (`EmailID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--
BEGIN;
INSERT INTO `User` VALUES (1, 'yjiang@ncsu.edu', 'Yuyang Jiang', '123456');
COMMIT;


LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-02 23:17:09

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
                        `EmployeeID` int NOT NULL,
                        `Name` varchar(45) DEFAULT NULL,
                        `Age` varchar(45) DEFAULT NULL,
                        `Skill` varchar(45) DEFAULT NULL,
                        `Telephone` varchar(45) DEFAULT NULL,
                        `Title` varchar(45) DEFAULT NULL,
                        PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

BEGIN;
INSERT INTO `Employee` VALUES (1, 'Das', '28', 'Java', '919919919', 'Software Engineer');
COMMIT;

DROP TABLE IF EXISTS `Task_Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Task_Employee` (
                            `EmployeeID` int NOT NULL,
                            `TaskID` int NOT NULL,
                            PRIMARY KEY (`EmployeeID`, `TaskID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

BEGIN;
INSERT INTO `Task_Employee` VALUES (1, 1);
COMMIT;



DROP TABLE IF EXISTS `Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Project` (
                            `ProjectID` int NOT NULL,
                            `ProjectName` varchar(45) DEFAULT NULL,
                            `Description` varchar(45) DEFAULT NULL,
                            `Technology` varchar(45) DEFAULT NULL,
                            PRIMARY KEY (`ProjectID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

BEGIN;
INSERT INTO `Project` VALUES (1, 'TeamFormation', 'Match team and proj', 'Python, JS');
COMMIT;

DROP TABLE IF EXISTS `Task_Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Task_Project` (
                                 `ProjectID` int NOT NULL,
                                 `TaskID` int NOT NULL,
                                 PRIMARY KEY (`ProjectID`, `TaskID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

BEGIN;
INSERT INTO `Task_Project` VALUES (1, 1);
COMMIT;
