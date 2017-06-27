-- MySQL dump 10.13  Distrib 5.6.13, for Win64 (x86_64)
--
-- Host: localhost    Database: flaskdb
-- ------------------------------------------------------
-- Server version	5.6.13-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alarm_record`
--

DROP TABLE IF EXISTS `alarm_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alarm_record` (
  `id` varchar(64) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `pdm_sn` varchar(32) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` varchar(8) DEFAULT NULL,
  `alarm_id` varchar(16) DEFAULT NULL,
  `alarm_param` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alarm_record`
--

LOCK TABLES `alarm_record` WRITE;
/*!40000 ALTER TABLE `alarm_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `alarm_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `basal_record`
--

DROP TABLE IF EXISTS `basal_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `basal_record` (
  `id` varchar(64) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `pdm_sn` varchar(32) DEFAULT NULL,
  `pump_sn` varchar(32) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` varchar(8) DEFAULT NULL,
  `duration` smallint(6) DEFAULT NULL,
  `rate` smallint(6) DEFAULT NULL,
  `inject` smallint(6) DEFAULT NULL,
  `param` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basal_record`
--

LOCK TABLES `basal_record` WRITE;
/*!40000 ALTER TABLE `basal_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `basal_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blood_glucose_record`
--

DROP TABLE IF EXISTS `blood_glucose_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blood_glucose_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `glucose` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blood_glucose_record`
--

LOCK TABLES `blood_glucose_record` WRITE;
/*!40000 ALTER TABLE `blood_glucose_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `blood_glucose_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bolus_record`
--

DROP TABLE IF EXISTS `bolus_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bolus_record` (
  `id` varchar(64) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `pdm_sn` varchar(32) DEFAULT NULL,
  `pump_sn` varchar(32) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` varchar(8) DEFAULT NULL,
  `normal_set` float DEFAULT NULL,
  `normal_inject` float DEFAULT NULL,
  `extend_set` float DEFAULT NULL,
  `extend_inject` float DEFAULT NULL,
  `extend_duration` smallint(6) DEFAULT NULL,
  `state` smallint(6) DEFAULT NULL,
  `wizard` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bolus_record`
--

LOCK TABLES `bolus_record` WRITE;
/*!40000 ALTER TABLE `bolus_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `bolus_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calib_record`
--

DROP TABLE IF EXISTS `calib_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calib_record` (
  `id` varchar(64) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `sensor_id` varchar(64) DEFAULT NULL,
  `sensor_progress_id` int(11) DEFAULT NULL,
  `type` varchar(8) DEFAULT NULL,
  `calib_time` datetime DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `signal_value` float DEFAULT NULL,
  `glucose_value` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calib_record`
--

LOCK TABLES `calib_record` WRITE;
/*!40000 ALTER TABLE `calib_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `calib_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device_settings`
--

DROP TABLE IF EXISTS `device_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `device_settings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `state` smallint(6) DEFAULT NULL,
  `settings` varchar(8192) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device_settings`
--

LOCK TABLES `device_settings` WRITE;
/*!40000 ALTER TABLE `device_settings` DISABLE KEYS */;
/*!40000 ALTER TABLE `device_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diabetes_info`
--

DROP TABLE IF EXISTS `diabetes_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diabetes_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `glucose_target` varchar(1024) DEFAULT NULL,
  `hypo` float DEFAULT NULL,
  `type` varchar(16) DEFAULT NULL,
  `confirm_time` varchar(16) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diabetes_info`
--

LOCK TABLES `diabetes_info` WRITE;
/*!40000 ALTER TABLE `diabetes_info` DISABLE KEYS */;
INSERT INTO `diabetes_info` VALUES (1,1,'[[0, 3.3, 8.4]]',3.3,NULL,NULL,'2015-05-21 14:09:40'),(2,2,'[[0, 3.3, 8.4]]',3.3,NULL,NULL,'2015-05-21 16:07:18'),(3,3,'[[0, 3.3, 8.4]]',3.3,NULL,NULL,'2015-05-21 16:18:10'),(4,4,'[[0, 3.3, 8.4]]',3.3,NULL,NULL,'2015-05-29 15:22:57'),(5,6,'[[0, 3.3, 8.4]]',3.3,NULL,NULL,'2015-07-07 12:55:12'),(6,7,'[[0, 3.3, 8.4]]',3.3,NULL,NULL,'2015-07-08 09:17:33'),(7,8,'[[0, 3.3, 8.4]]',3.3,NULL,NULL,'2015-07-08 10:43:15');
/*!40000 ALTER TABLE `diabetes_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_info`
--

DROP TABLE IF EXISTS `doctor_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctor_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `major` varchar(64) DEFAULT NULL,
  `title` varchar(64) DEFAULT NULL,
  `serve_for` varchar(64) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_info`
--

LOCK TABLES `doctor_info` WRITE;
/*!40000 ALTER TABLE `doctor_info` DISABLE KEYS */;
INSERT INTO `doctor_info` VALUES (1,5,NULL,NULL,NULL,'2015-06-10 16:25:17');
/*!40000 ALTER TABLE `doctor_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_log`
--

DROP TABLE IF EXISTS `event_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `event` varchar(20) DEFAULT NULL,
  `detail` varchar(30) DEFAULT NULL,
  `remark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_event_log_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_log`
--

LOCK TABLES `event_log` WRITE;
/*!40000 ALTER TABLE `event_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `event_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_record`
--

DROP TABLE IF EXISTS `event_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event_record` (
  `id` varchar(64) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `pdm_sn` varchar(32) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` varchar(8) DEFAULT NULL,
  `content` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_record`
--

LOCK TABLES `event_record` WRITE;
/*!40000 ALTER TABLE `event_record` DISABLE KEYS */;
INSERT INTO `event_record` VALUES ('jUVKM3r06LNBxzs8OgHm',8,NULL,'2015-07-08 10:50:00','食物','{\"remark\": \"ggdasg\", \"timeclick\": 1, \"detail\": \"200g\", \"dateorder\": \"descending\", \"timeorder\": \"descending\", \"eventorder\": \"descending\", \"eventclick\": 0}'),('pOdsvfCzP7LmRYNtnr1X',4,NULL,'2015-05-29 15:23:00','食物','{\"remark\": \"蛋糕\", \"timeclick\": 1, \"detail\": \"200g\", \"dateorder\": \"descending\", \"timeorder\": \"descending\", \"eventorder\": \"descending\", \"eventclick\": 0}');
/*!40000 ALTER TABLE `event_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mail`
--

DROP TABLE IF EXISTS `mail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `state` varchar(16) DEFAULT NULL,
  `title` varchar(256) DEFAULT NULL,
  `body` text,
  `time` datetime DEFAULT NULL,
  `flag` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mail`
--

LOCK TABLES `mail` WRITE;
/*!40000 ALTER TABLE `mail` DISABLE KEYS */;
/*!40000 ALTER TABLE `mail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrate_version`
--

DROP TABLE IF EXISTS `migrate_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `migrate_version` (
  `repository_id` varchar(250) NOT NULL,
  `repository_path` text,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`repository_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrate_version`
--

LOCK TABLES `migrate_version` WRITE;
/*!40000 ALTER TABLE `migrate_version` DISABLE KEYS */;
INSERT INTO `migrate_version` VALUES ('database repository','D:\\Projects\\Python\\TrumCloud\\db_repository',20);
/*!40000 ALTER TABLE `migrate_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitor_info`
--

DROP TABLE IF EXISTS `monitor_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitor_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `state` varchar(128) DEFAULT NULL,
  `glucose` float DEFAULT NULL,
  `bolus` float DEFAULT NULL,
  `basal` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitor_info`
--

LOCK TABLES `monitor_info` WRITE;
/*!40000 ALTER TABLE `monitor_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitor_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pdf_download_record`
--

DROP TABLE IF EXISTS `pdf_download_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pdf_download_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `pdf_type` varchar(64) DEFAULT NULL,
  `file_uuid` varchar(128) DEFAULT NULL,
  `params` varchar(128) DEFAULT NULL,
  `dependency` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pdf_download_record`
--

LOCK TABLES `pdf_download_record` WRITE;
/*!40000 ALTER TABLE `pdf_download_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `pdf_download_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_info`
--

DROP TABLE IF EXISTS `personal_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personal_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `realname` varchar(64) DEFAULT NULL,
  `nickname` varchar(64) DEFAULT NULL,
  `gender` varchar(8) DEFAULT NULL,
  `marriage` varchar(8) DEFAULT NULL,
  `birth_date` varchar(16) DEFAULT NULL,
  `cert_type` varchar(16) DEFAULT NULL,
  `cert_id` varchar(64) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `province` varchar(128) DEFAULT NULL,
  `city` varchar(128) DEFAULT NULL,
  `county` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `zipcode` varchar(8) DEFAULT NULL,
  `motto` varchar(200) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `portrait` varchar(64) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_personal_info_cert_id` (`cert_id`),
  UNIQUE KEY `ix_personal_info_nickname` (`nickname`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_info`
--

LOCK TABLES `personal_info` WRITE;
/*!40000 ALTER TABLE `personal_info` DISABLE KEYS */;
INSERT INTO `personal_info` VALUES (1,1,'123123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2015-05-21 14:09:40'),(2,2,'陆洁',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2015-05-21 16:07:18'),(3,3,'person',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2015-05-21 16:18:10'),(4,4,'123123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2015-05-29 15:22:57'),(5,5,'123123',NULL,'男',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2015-06-10 16:25:17'),(6,6,'asdfasdf',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2015-07-07 12:55:12'),(7,7,'123asdf',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2015-07-08 09:17:33'),(8,8,'陆洁',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2015-07-08 10:43:15');
/*!40000 ALTER TABLE `personal_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preference`
--

DROP TABLE IF EXISTS `preference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `preference` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) DEFAULT NULL,
  `style` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preference`
--

LOCK TABLES `preference` WRITE;
/*!40000 ALTER TABLE `preference` DISABLE KEYS */;
/*!40000 ALTER TABLE `preference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relation`
--

DROP TABLE IF EXISTS `relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `relation` (
  `subject` int(11) NOT NULL AUTO_INCREMENT,
  `object` int(11) NOT NULL,
  `privilege` varchar(8) DEFAULT NULL,
  `last_visit` datetime DEFAULT NULL,
  PRIMARY KEY (`subject`,`object`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relation`
--

LOCK TABLES `relation` WRITE;
/*!40000 ALTER TABLE `relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor_event`
--

DROP TABLE IF EXISTS `sensor_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensor_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `sensor_id` varchar(32) DEFAULT NULL,
  `sensor_progress_id` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `event_type` varchar(32) DEFAULT NULL,
  `event_state` varchar(32) DEFAULT NULL,
  `event_value` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor_event`
--

LOCK TABLES `sensor_event` WRITE;
/*!40000 ALTER TABLE `sensor_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensor_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor_glucose_record`
--

DROP TABLE IF EXISTS `sensor_glucose_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensor_glucose_record` (
  `id` varchar(64) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `sensor_id` varchar(64) DEFAULT NULL,
  `session_id` varchar(64) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `sensor_state` varchar(4) DEFAULT NULL,
  `glucose_value` float DEFAULT NULL,
  `signal_value` float DEFAULT NULL,
  `rate` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor_glucose_record`
--

LOCK TABLES `sensor_glucose_record` WRITE;
/*!40000 ALTER TABLE `sensor_glucose_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensor_glucose_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor_progress`
--

DROP TABLE IF EXISTS `sensor_progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensor_progress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `sensor_id` varchar(64) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `readings` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor_progress`
--

LOCK TABLES `sensor_progress` WRITE;
/*!40000 ALTER TABLE `sensor_progress` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensor_progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_table`
--

DROP TABLE IF EXISTS `test_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hypo` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_table`
--

LOCK TABLES `test_table` WRITE;
/*!40000 ALTER TABLE `test_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upload_record`
--

DROP TABLE IF EXISTS `upload_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `upload_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `pdm_sn` varchar(32) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upload_record`
--

LOCK TABLES `upload_record` WRITE;
/*!40000 ALTER TABLE `upload_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `upload_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `last_visit` datetime DEFAULT NULL,
  `state` varchar(16) DEFAULT NULL,
  `type` varchar(8) DEFAULT NULL,
  `mibao` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'asdfasf','123123','2015-05-21 14:09:40','2015-05-21 14:09:40','A','P',NULL),(2,'janelle','Hi1188,.','2015-05-21 16:07:18','2015-05-21 16:07:18','A','P',NULL),(3,'person','123456','2015-05-21 16:18:10','2015-05-21 16:18:10','A','P',NULL),(4,'person_test10','123123','2015-05-29 15:22:57','2015-05-29 15:22:57','A','P',NULL),(5,'doctor1','123123','2015-06-10 16:25:17','2015-06-10 16:25:17','A','D',NULL),(6,'person_test26','123123','2015-07-07 12:55:12','2015-07-07 12:55:12','A','P',NULL),(7,'sdsdfasdfsadf','123123','2015-07-08 09:17:33','2015-07-08 09:17:33','A','P',NULL),(8,'jose6','HicCup1188','2015-07-08 10:43:15','2015-07-08 10:43:15','A','P',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-09 19:16:53
