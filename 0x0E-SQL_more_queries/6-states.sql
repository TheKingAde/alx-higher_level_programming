-- create the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS `htbn_0d_usa`;
CREATE TABLE IF NOT EXISTS `htbn_0d_usa`.`states` (
	`id` INT AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`)
);
