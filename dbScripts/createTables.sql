CREATE TABLE `sensorValues` (
  `idRecord` int NOT NULL AUTO_INCREMENT,
  `idDevice` int DEFAULT NULL,
  `idSensor` int DEFAULT NULL,
  `valueType` int DEFAULT NULL,
  `valueSensor` float DEFAULT NULL,
  `tStamp` datetime DEFAULT NULL,
  `tStampSensor` datetime DEFAULT NULL,
  PRIMARY KEY (`idRecord`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `devices` (
  `iddevices` int NOT NULL AUTO_INCREMENT,
  `dvName` varchar(45) NOT NULL,
  `dvLocation` varchar(45) NOT NULL,
  `sensNumber` int NOT NULL,
  PRIMARY KEY (`iddevices`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `valuesType` (
  `idvaluesType` int NOT NULL AUTO_INCREMENT,
  `type` varchar(45) DEFAULT NULL,
  `um` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idvaluesType`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `iot`.`valuesType` (`idvaluesType`, `type`, `um`) VALUES (1, "Temperature", "C");
INSERT INTO `iot`.`valuesType` (`idvaluesType`, `type`, `um`) VALUES (2, "Humidity", "%");
INSERT INTO `iot`.`valuesType` (`idvaluesType`, `type`, `um`) VALUES (3, "Pressure", "Bar");
