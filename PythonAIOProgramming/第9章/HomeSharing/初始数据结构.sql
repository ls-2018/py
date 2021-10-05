-- 第9章/HomeSharing/初始数据结构.sql

SET NAMES utf8;
SET
time_zone = '+00:00';
SET
foreign_key_checks = 0;
SET
sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `role`        tinytext NOT NULL,
    `description` tinytext NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `role` (`role`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `auth_membership`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`
(
    `id`            int(11) NOT NULL AUTO_INCREMENT,
    `user_name`     tinytext    NOT NULL,
    `user_password` varchar(64) NOT NULL,
    `user_email`    tinytext    NOT NULL,
    `user_phone`    varchar(16) NOT NULL,
    `reg_time`      datetime    NOT NULL DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (`id`),
    UNIQUE KEY `user_phone` (`user_phone`),
    UNIQUE KEY `user_name` (`user_name`) USING HASH,
    UNIQUE KEY `user_email` (`user_email`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `house_res`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `house_res_comment`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `photo`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;