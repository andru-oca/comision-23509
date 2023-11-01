-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: libreria_23509
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `AUTOR`
--

DROP TABLE IF EXISTS `AUTOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AUTOR` (
  `CODIGO_AUTOR` int NOT NULL AUTO_INCREMENT,
  `NOMBRE` varchar(50) DEFAULT 'NO NAME FOUND',
  PRIMARY KEY (`CODIGO_AUTOR`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AUTOR`
--

LOCK TABLES `AUTOR` WRITE;
/*!40000 ALTER TABLE `AUTOR` DISABLE KEYS */;
INSERT INTO `AUTOR` VALUES (1,'FLAVIA'),(2,'CAROLINA'),(3,'ARTURO'),(4,'LARA'),(5,'Conrade'),(6,'Gertrudis'),(7,'Travus'),(8,'Myrtice'),(9,'Jonathon'),(10,'Penny'),(11,'Lucian'),(12,'Beret'),(13,'Stephannie'),(14,'Winnie'),(15,'Kristine'),(16,'Tybi'),(17,'Gilligan'),(18,'Ilsa'),(19,'Jordon'),(20,'Stevana'),(21,'Terza'),(22,'Laurene'),(23,NULL),(24,'Esdras'),(25,'Zeb'),(26,'Mick'),(27,'Ricardo'),(28,'Hestia'),(29,'Errick'),(30,'Celeste'),(31,'Doug'),(32,'Barde'),(33,'Joachim'),(34,NULL),(35,'Jayme'),(36,'West'),(37,'Stephani'),(38,'Ellen'),(39,'Corie'),(40,'Riordan'),(41,'Kalinda'),(42,NULL),(43,'Allene'),(44,'Dre'),(45,'Karlene'),(46,'Livvie'),(47,'Teri'),(48,'Melania'),(49,'Ritchie'),(50,'Ginelle'),(51,'Jocelyne'),(52,'Hilary'),(53,'Ezechiel'),(54,'Roxi'),(55,'Lind'),(56,'Ursala'),(57,'Jesse'),(58,NULL),(59,'Andriana'),(60,'Kylynn'),(61,'Cammi'),(62,'Shirline'),(63,NULL),(64,'Emyle'),(65,'Chucho'),(66,'Salli'),(67,'Mina'),(68,'Brittney'),(69,'Manfred'),(70,NULL),(71,'Celene'),(72,NULL),(73,'Erma'),(74,'Maison'),(75,NULL),(76,'Terrye'),(77,NULL),(78,'Emmery'),(79,'Kele'),(80,'Marc'),(81,'Charlie'),(82,'Cornelle'),(83,'Boyce'),(84,'Helene'),(85,'Devora'),(86,'Evangeline'),(87,'North'),(88,NULL),(89,'Arabella'),(90,'Flemming'),(91,'Dominga'),(92,NULL),(93,'Nolana'),(94,'Edvard'),(95,'Andrea'),(96,'Darb'),(97,'Dion'),(98,'Karlens'),(99,'Boot'),(100,'Liz'),(101,'Jessy'),(102,'Vivie'),(103,'Donall'),(104,'Leonard'),(105,'Vivie');
/*!40000 ALTER TABLE `AUTOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EJEMPLAR`
--

DROP TABLE IF EXISTS `EJEMPLAR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EJEMPLAR` (
  `CODIGO_EJEMPLAR` int NOT NULL AUTO_INCREMENT,
  `CODIGO_LIBRO` int NOT NULL,
  `ALMACEN` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CODIGO_EJEMPLAR`),
  KEY `CODIGO_LIBRO` (`CODIGO_LIBRO`),
  CONSTRAINT `EJEMPLAR_ibfk_1` FOREIGN KEY (`CODIGO_LIBRO`) REFERENCES `LIBRO` (`CODIGO_LIBRO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EJEMPLAR`
--

LOCK TABLES `EJEMPLAR` WRITE;
/*!40000 ALTER TABLE `EJEMPLAR` DISABLE KEYS */;
/*!40000 ALTER TABLE `EJEMPLAR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIBRO`
--

DROP TABLE IF EXISTS `LIBRO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LIBRO` (
  `CODIGO_LIBRO` int NOT NULL AUTO_INCREMENT,
  `ISBN` varchar(100) DEFAULT '987-ISBN-PIRULO',
  `TITULO` varchar(100) NOT NULL,
  `EDITORIAL` varchar(100) DEFAULT NULL,
  `PAGINAS` int DEFAULT '100',
  PRIMARY KEY (`CODIGO_LIBRO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIBRO`
--

LOCK TABLES `LIBRO` WRITE;
/*!40000 ALTER TABLE `LIBRO` DISABLE KEYS */;
/*!40000 ALTER TABLE `LIBRO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LINK_AUTOR_LIBRO`
--

DROP TABLE IF EXISTS `LINK_AUTOR_LIBRO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LINK_AUTOR_LIBRO` (
  `CODIGO_AUTOR` int NOT NULL,
  `CODIGO_LIBRO` int NOT NULL,
  `LUGAR_ESCRITURA` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CODIGO_AUTOR`,`CODIGO_LIBRO`),
  KEY `CODIGO_LIBRO` (`CODIGO_LIBRO`),
  CONSTRAINT `LINK_AUTOR_LIBRO_ibfk_1` FOREIGN KEY (`CODIGO_AUTOR`) REFERENCES `AUTOR` (`CODIGO_AUTOR`),
  CONSTRAINT `LINK_AUTOR_LIBRO_ibfk_2` FOREIGN KEY (`CODIGO_LIBRO`) REFERENCES `LIBRO` (`CODIGO_LIBRO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LINK_AUTOR_LIBRO`
--

LOCK TABLES `LINK_AUTOR_LIBRO` WRITE;
/*!40000 ALTER TABLE `LINK_AUTOR_LIBRO` DISABLE KEYS */;
/*!40000 ALTER TABLE `LINK_AUTOR_LIBRO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USUARIO`
--

DROP TABLE IF EXISTS `USUARIO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USUARIO` (
  `ID_USUARIO` int NOT NULL AUTO_INCREMENT,
  `NOMBRE` varchar(50) DEFAULT NULL,
  `TEL` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `DIRECCION` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_USUARIO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USUARIO`
--

LOCK TABLES `USUARIO` WRITE;
/*!40000 ALTER TABLE `USUARIO` DISABLE KEYS */;
/*!40000 ALTER TABLE `USUARIO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VENTA`
--

DROP TABLE IF EXISTS `VENTA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `VENTA` (
  `ID_VENTA` int NOT NULL AUTO_INCREMENT,
  `CODIGO_EJEMPLAR` int NOT NULL,
  `ID_USUARIO` int NOT NULL,
  `PUNTO_VENTA` varchar(100) DEFAULT NULL,
  `PRECIO_VENTA` decimal(10,2) DEFAULT NULL,
  `FECHA_VENTA` datetime DEFAULT NULL,
  PRIMARY KEY (`ID_VENTA`),
  KEY `CODIGO_EJEMPLAR` (`CODIGO_EJEMPLAR`),
  KEY `ID_USUARIO` (`ID_USUARIO`),
  CONSTRAINT `VENTA_ibfk_1` FOREIGN KEY (`CODIGO_EJEMPLAR`) REFERENCES `EJEMPLAR` (`CODIGO_EJEMPLAR`),
  CONSTRAINT `VENTA_ibfk_2` FOREIGN KEY (`ID_USUARIO`) REFERENCES `USUARIO` (`ID_USUARIO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VENTA`
--

LOCK TABLES `VENTA` WRITE;
/*!40000 ALTER TABLE `VENTA` DISABLE KEYS */;
/*!40000 ALTER TABLE `VENTA` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-27 18:29:20
