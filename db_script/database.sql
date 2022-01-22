-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.17-log - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for database
CREATE DATABASE IF NOT EXISTS `database` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `database`;

-- Dumping structure for table database.college_list
CREATE TABLE IF NOT EXISTS `college_list` (
  `college_code` varchar(50) NOT NULL,
  `college_name` varchar(50) NOT NULL,
  PRIMARY KEY (`college_code`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table database.college_list: ~6 rows (approximately)
/*!40000 ALTER TABLE `college_list` DISABLE KEYS */;
INSERT INTO `college_list` (`college_code`, `college_name`) VALUES
	('College of Arts and Social Sciences', 'CASS'),
	('College of Business Administration and Accountancy', 'CBAA'),
	('College of Computer Studies', 'CCS'),
	('College of Education', 'CED'),
	('College of Engineering and Technology', 'COET'),
	('School of Engineering Technology', 'SET');
/*!40000 ALTER TABLE `college_list` ENABLE KEYS */;

-- Dumping structure for table database.course_list
CREATE TABLE IF NOT EXISTS `course_list` (
  `course_code` varchar(50) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `college` varchar(50) NOT NULL,
  PRIMARY KEY (`course_code`),
  KEY `college` (`college`),
  CONSTRAINT `college` FOREIGN KEY (`college`) REFERENCES `college_list` (`college_code`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table database.course_list: ~4 rows (approximately)
/*!40000 ALTER TABLE `course_list` DISABLE KEYS */;
INSERT INTO `course_list` (`course_code`, `course_name`, `college`) VALUES
	('BSCA', 'Bachelor of Science in Computer Applications', 'College of Computer Studies'),
	('BSCE', 'Bachelor of Science in Civil Engineering', 'College of Engineering and Technology'),
	('BSCS', 'Bachelor of Science in Computer Science', 'College of Computer Studies'),
	('BSIT', 'Bachelor of Science in Information Technology', 'College of Engineering and Technology');
/*!40000 ALTER TABLE `course_list` ENABLE KEYS */;

-- Dumping structure for table database.student_list
CREATE TABLE IF NOT EXISTS `student_list` (
  `stud_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) NOT NULL DEFAULT '0',
  `lname` varchar(50) NOT NULL DEFAULT '0',
  `course` varchar(50) NOT NULL DEFAULT '0',
  `year_lvl` varchar(50) NOT NULL DEFAULT '0',
  `gender` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`stud_id`),
  KEY `FK__course_list` (`course`),
  CONSTRAINT `FK__course_list` FOREIGN KEY (`course`) REFERENCES `course_list` (`course_code`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20210002 DEFAULT CHARSET=utf8;

-- Dumping data for table database.student_list: ~2 rows (approximately)
/*!40000 ALTER TABLE `student_list` DISABLE KEYS */;
INSERT INTO `student_list` (`stud_id`, `fname`, `lname`, `course`, `year_lvl`, `gender`) VALUES
	(20151595, 'Naruto', 'Uzumaki', 'BSCS', '4', 'M'),
	(20210001, 'Jungkook', 'Jeon', 'BSCA', '1', 'M');
/*!40000 ALTER TABLE `student_list` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
