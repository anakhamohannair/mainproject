/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.7.31 : Database - breastcancer
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`breastcancer` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `breastcancer`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `Feedid` int(11) NOT NULL AUTO_INCREMENT,
  `Userid` int(11) DEFAULT NULL,
  `Feedback` varchar(30) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Feedid`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`Feedid`,`Userid`,`Feedback`,`Date`) values (1,2,'best exp ever','2022-04-08');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `LoginID` int(30) NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) DEFAULT NULL,
  `Password` varchar(30) DEFAULT NULL,
  `Type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`LoginID`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`LoginID`,`Username`,`Password`,`Type`) values (1,'Neeraja','123456@','Admin'),(3,'qwerty','123','user'),(7,'surya','1234567@','user');

/*Table structure for table `registration` */

DROP TABLE IF EXISTS `registration`;

CREATE TABLE `registration` (
  `Regid` int(11) NOT NULL AUTO_INCREMENT,
  `LoginID` int(11) DEFAULT NULL,
  `Fname` varchar(30) DEFAULT NULL,
  `Lname` varchar(30) DEFAULT NULL,
  `Place` varchar(30) DEFAULT NULL,
  `Post` varchar(30) DEFAULT NULL,
  `Pin` bigint(20) DEFAULT NULL,
  `phoneno` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Regid`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `registration` */

insert  into `registration`(`Regid`,`LoginID`,`Fname`,`Lname`,`Place`,`Post`,`Pin`,`phoneno`,`email`) values (1,2,'qwer','qwer','qwert','wert',1234,4567,'qwer@qw.qwer'),(2,5,'neeraja','aj','kkm','gvr',680542,9061668599,'dayasathyan916@gmail.com'),(3,6,'Sarath','Viswanath','kkm','gvr',680542,9061668599,'dayasathyan916@gmail.com'),(4,7,'Surya','K','CKM','gvr',680542,7012524831,'suryaviswanath79@gmail.com');

/*Table structure for table `tip` */

DROP TABLE IF EXISTS `tip`;

CREATE TABLE `tip` (
  `Tipid` bigint(20) NOT NULL AUTO_INCREMENT,
  `Tip` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Tipid`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `tip` */

insert  into `tip`(`Tipid`,`Tip`) values (0,'cythjfngdbfs'),(7,'vng,jgk,ycfdt');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
