-- MariaDB dump 10.17  Distrib 10.5.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: home_sharing
-- ------------------------------------------------------
-- Server version	10.5.6-MariaDB-1:10.5.6+maria~focal

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `home_sharing`
--

CREATE
DATABASE /*!32312 IF NOT EXISTS*/ `home_sharing` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE
`home_sharing`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `role`        tinytext NOT NULL,
    `description` tinytext NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `role` (`role`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK
TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group`
VALUES (1, 'admin', '管理员'),
       (2, 'edtior', '编辑者');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK
TABLES;

--
-- Table structure for table `auth_membership`
--

DROP TABLE IF EXISTS `auth_membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_membership`
(
    `id`       int(11) NOT NULL AUTO_INCREMENT,
    `group_id` int(11) NOT NULL,
    `user_id`  int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY        `group_id` (`group_id`),
    KEY        `user_id` (`user_id`),
    CONSTRAINT `auth_membership_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
    CONSTRAINT `auth_membership_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_membership`
--

LOCK
TABLES `auth_membership` WRITE;
/*!40000 ALTER TABLE `auth_membership` DISABLE KEYS */;
INSERT INTO `auth_membership`
VALUES (12, 1, 13),
       (15, 1, 12);
/*!40000 ALTER TABLE `auth_membership` ENABLE KEYS */;
UNLOCK
TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user`
(
    `id`            int(11) NOT NULL AUTO_INCREMENT,
    `user_name`     tinytext     NOT NULL,
    `user_password` varchar(128) NOT NULL,
    `user_email`    tinytext     NOT NULL,
    `user_phone`    varchar(16)  NOT NULL,
    `reg_time`      datetime     NOT NULL DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (`id`),
    UNIQUE KEY `user_phone` (`user_phone`),
    UNIQUE KEY `user_name` (`user_name`) USING HASH,
    UNIQUE KEY `user_email` (`user_email`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK
TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user`
VALUES (6, 'a', 'pbkdf2(1000,20,sha512)$a0e70e2e5b3eb9ba$7f9b0b76534455e5cb4af600062ee0f2afb96cc4', 'a@a.a', 'a',
        '2020-11-01 04:46:36'),
       (11, 'b', 'pbkdf2(1000,20,sha512)$847063748ff05d39$149777b1f23cdff92e4f23e309423280d3908779', 'a@a.a1', 'b',
        '2020-11-02 01:08:56'),
       (12, 'cms4py', 'pbkdf2(1000,20,sha512)$9317c4611014e61a$ddcf70c0277f20934970adc8c9b24039cedb34ad',
        'cms4py@cms4py.org', '13000000000', '2020-11-03 07:33:29'),
       (13, 'admin', 'pbkdf2(1000,20,sha512)$a5989c00103268bb$809abf2086073d2665c3eed684b182007448e695',
        'admin@admin.admin', '13800000000', '2020-11-05 01:54:30');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK
TABLES;

--
-- Table structure for table `house_res`
--

DROP TABLE IF EXISTS `house_res`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `house_res`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `res_title`   tinytext NOT NULL,
    `res_content` longtext NOT NULL,
    `pub_time`    datetime NOT NULL,
    `owner_id`    int(11) NOT NULL,
    PRIMARY KEY (`id`),
    KEY           `owner_id` (`owner_id`),
    CONSTRAINT `house_res_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `house_res`
--

LOCK
TABLES `house_res` WRITE;
/*!40000 ALTER TABLE `house_res` DISABLE KEYS */;
INSERT INTO `house_res`
VALUES (2, '第二个房子', '<p>asxasx</p><p>cdsc</p><p>csd</p>', '2020-11-06 17:02:01', 13),
       (4, '海淀正规小区整租',
        '<p>海淀正规小区整租，要求租户必须是程序员</p><figure class=\"image\"><img src=\"/static_files/uploads/u13d20201106221254451075\"></figure>',
        '2020-11-06 22:13:16', 13),
       (5, '正规三居出租', '<p>正规三居出租，无图有真相，电话联系我。</p>', '2020-11-07 10:39:23', 13),
       (6, '单独民房带独卫', '<p>超值民房出租</p>', '2020-11-07 10:40:22', 13),
       (7, '精装1居室出租', '<p>精装，第一次出租</p>', '2020-11-07 10:41:31', 13);
/*!40000 ALTER TABLE `house_res` ENABLE KEYS */;
UNLOCK
TABLES;

--
-- Table structure for table `house_res_comment`
--

DROP TABLE IF EXISTS `house_res_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `house_res_comment`
(
    `id`              int(11) NOT NULL AUTO_INCREMENT,
    `user_id`         int(11) NOT NULL,
    `house_res_id`    int(11) NOT NULL,
    `comment_content` text     NOT NULL,
    `comment_time`    datetime NOT NULL,
    PRIMARY KEY (`id`),
    KEY               `user_id` (`user_id`),
    KEY               `house_res_id` (`house_res_id`),
    CONSTRAINT `house_res_comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
    CONSTRAINT `house_res_comment_ibfk_2` FOREIGN KEY (`house_res_id`) REFERENCES `house_res` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `house_res_comment`
--

LOCK
TABLES `house_res_comment` WRITE;
/*!40000 ALTER TABLE `house_res_comment` DISABLE KEYS */;
INSERT INTO `house_res_comment`
VALUES (1, 13, 7, '<p>好房源</p>', '2020-11-07 12:56:40'),
       (2, 13, 7, '<p>好房源</p>', '2020-11-07 13:35:40'),
       (3, 13, 7, '<p>明天去看看</p>', '2020-11-07 13:37:21');
/*!40000 ALTER TABLE `house_res_comment` ENABLE KEYS */;
UNLOCK
TABLES;

--
-- Table structure for table `photo`
--

DROP TABLE IF EXISTS `photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `photo`
(
    `id`            int(11) NOT NULL AUTO_INCREMENT,
    `photo_name`    tinytext NOT NULL,
    `photo_uri`     tinytext NOT NULL,
    `photo_path`    tinytext NOT NULL,
    `creator`       int(11) NOT NULL,
    `creation_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (`id`),
    KEY             `creator` (`creator`),
    CONSTRAINT `photo_ibfk_1` FOREIGN KEY (`creator`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photo`
--

LOCK
TABLES `photo` WRITE;
/*!40000 ALTER TABLE `photo` DISABLE KEYS */;
INSERT INTO `photo`
VALUES (1, '4636003.jpg', '/static_files/uploads/u13d20201106151720355164', 'u13d20201106151720355164', 13,
        '2020-11-06 15:17:20'),
       (2, '4636003.jpg', '/static_files/uploads/u13d20201106163053183534', 'u13d20201106163053183534', 13,
        '2020-11-06 16:30:53'),
       (3, '4636003.jpg', '/static_files/uploads/u13d20201106163241482308', 'u13d20201106163241482308', 13,
        '2020-11-06 16:32:41'),
       (4, 'WechatIMG9.jpeg', '/static_files/uploads/u13d20201106173131571218', 'u13d20201106173131571218', 13,
        '2020-11-06 17:31:31'),
       (5, 'WechatIMG9.jpeg', '/static_files/uploads/u13d20201106210646819425', 'u13d20201106210646819425', 13,
        '2020-11-06 21:06:46'),
       (6, 'house.jpg', '/static_files/uploads/u13d20201106221254451075', 'u13d20201106221254451075', 13,
        '2020-11-06 22:12:54');
/*!40000 ALTER TABLE `photo` ENABLE KEYS */;
UNLOCK
TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-08  0:49:03
