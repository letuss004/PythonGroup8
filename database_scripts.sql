-- MySQL Script generated by MySQL Workbench
-- Thu May 20 11:58:05 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema hotel
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `hotel` ;

-- -----------------------------------------------------
-- Schema hotel
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotel` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `hotel` ;

-- -----------------------------------------------------
-- Table `hotel`.`customer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`customer` ;

CREATE TABLE IF NOT EXISTS `hotel`.`customer` (
  `id` VARCHAR(45) NOT NULL,
  `full_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`room_status`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`room_status` ;

CREATE TABLE IF NOT EXISTS `hotel`.`room_status` (
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`status`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`room_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`room_type` ;

CREATE TABLE IF NOT EXISTS `hotel`.`room_type` (
  `types` VARCHAR(45) NOT NULL,
  `price` INT NOT NULL,
  PRIMARY KEY (`types`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`room`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`room` ;

CREATE TABLE IF NOT EXISTS `hotel`.`room` (
  `id` VARCHAR(45) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `type_fk_idx` (`type` ASC) VISIBLE,
  INDEX `status_fk_idx` (`status` ASC) VISIBLE,
  CONSTRAINT `status_fk`
    FOREIGN KEY (`status`)
    REFERENCES `hotel`.`room_status` (`status`),
  CONSTRAINT `type_fk`
    FOREIGN KEY (`type`)
    REFERENCES `hotel`.`room_type` (`types`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`check_in`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`check_in` ;

CREATE TABLE IF NOT EXISTS `hotel`.`check_in` (
  `check_in_id` INT NOT NULL AUTO_INCREMENT,
  `room_id` VARCHAR(45) NOT NULL,
  `customer_id` VARCHAR(45) NOT NULL,
  `check_in_day` VARCHAR(45) NOT NULL DEFAULT '0',
  PRIMARY KEY (`check_in_id`),
  INDEX `customer_id_fk_idx` (`customer_id` ASC) VISIBLE,
  INDEX `room_id_idx` (`room_id` ASC) VISIBLE,
  CONSTRAINT `customer_id_fk`
    FOREIGN KEY (`customer_id`)
    REFERENCES `hotel`.`customer` (`id`),
  CONSTRAINT `room_id_fk`
    FOREIGN KEY (`room_id`)
    REFERENCES `hotel`.`room` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 23
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`check_out`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`check_out` ;

CREATE TABLE IF NOT EXISTS `hotel`.`check_out` (
  `check_out_id` INT NOT NULL AUTO_INCREMENT,
  `check_in_id` INT NOT NULL,
  `check_out_day` VARCHAR(45) NOT NULL,
  `total_price` INT(10) UNSIGNED ZEROFILL NOT NULL,
  PRIMARY KEY (`check_out_id`),
  INDEX `check in id fk_idx` (`check_in_id` ASC) VISIBLE,
  CONSTRAINT `check in id fk`
    FOREIGN KEY (`check_in_id`)
    REFERENCES `hotel`.`check_in` (`check_in_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`history`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`history` ;

CREATE TABLE IF NOT EXISTS `hotel`.`history` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `check_in_id` INT NOT NULL,
  `check_out_id` INT NOT NULL,
  `check_in_date` VARCHAR(45) NOT NULL,
  `check_out_date` VARCHAR(45) NOT NULL,
  `price` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `check_in_fk_idx` (`check_in_id` ASC) VISIBLE,
  INDEX `check_out_fk_idx` (`check_out_id` ASC) VISIBLE,
  CONSTRAINT `check_in_fk`
    FOREIGN KEY (`check_in_id`)
    REFERENCES `hotel`.`check_in` (`check_in_id`),
  CONSTRAINT `check_out_fk`
    FOREIGN KEY (`check_out_id`)
    REFERENCES `hotel`.`check_out` (`check_out_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`supply`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`supply` ;

CREATE TABLE IF NOT EXISTS `hotel`.`supply` (
  `id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `price` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`room_service`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`room_service` ;

CREATE TABLE IF NOT EXISTS `hotel`.`room_service` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `check_in_id` INT NOT NULL,
  `supply_id` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `supply_id_fk_idx` (`supply_id` ASC) VISIBLE,
  INDEX `check in fk_idx` (`check_in_id` ASC) VISIBLE,
  CONSTRAINT `check in fk`
    FOREIGN KEY (`check_in_id`)
    REFERENCES `hotel`.`check_in` (`check_in_id`),
  CONSTRAINT `supply_id`
    FOREIGN KEY (`supply_id`)
    REFERENCES `hotel`.`supply` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 29
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
