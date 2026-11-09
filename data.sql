SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `play_store` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `play_store` ;

DROP TABLE IF EXISTS `play_store`.`library`;
DROP TABLE IF EXISTS `play_store`.`bills`;
DROP TABLE IF EXISTS `play_store`.`reviews`;
DROP TABLE IF EXISTS `play_store`.`payment_cards`;
DROP TABLE IF EXISTS `play_store`.`apps_categories`;
DROP TABLE IF EXISTS `play_store`.`categories`;
DROP TABLE IF EXISTS `play_store`.`apps_discounts`;
DROP TABLE IF EXISTS `play_store`.`apps_versions`;
DROP TABLE IF EXISTS `play_store`.`installations`;
DROP TABLE IF EXISTS `play_store`.`apps`;
DROP TABLE IF EXISTS `play_store`.`companies`;
DROP TABLE IF EXISTS `play_store`.`accounts_devices`;
DROP TABLE IF EXISTS `play_store`.`devices`;
DROP TABLE IF EXISTS `play_store`.`accounts`;

CREATE TABLE IF NOT EXISTS `play_store`.`accounts` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `name` VARCHAR(70) NOT NULL,
  `is_developer` TINYINT UNSIGNED NOT NULL DEFAULT 0,
  `country` VARCHAR(70) NOT NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `name` (`name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`devices` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `model` VARCHAR(45) NOT NULL,
  `os_version` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`accounts_devices` (
  `account_id` INT UNSIGNED NOT NULL,
  `device_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`account_id`, `device_id`),
  INDEX `accounts_devices_device1_id_fk_idx` (`device_id` ASC) VISIBLE,
  CONSTRAINT `accounts_devices_account2_id_fk`
    FOREIGN KEY (`account_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `accounts_devices_device1_id_fk`
    FOREIGN KEY (`device_id`)
    REFERENCES `play_store`.`devices` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`companies` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `company_name` VARCHAR(60) NOT NULL,
  `contact_email` VARCHAR(255) NULL,
  `developer_account_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `company_name_UNIQUE` (`company_name` ASC) VISIBLE,
  UNIQUE INDEX `developer_account_id_UNIQUE` (`developer_account_id` ASC) VISIBLE,
  CONSTRAINT `fk_companies_developer_account`
    FOREIGN KEY (`developer_account_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`apps` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(80) NOT NULL,
  `caption` VARCHAR(600) NULL,
  `price` DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  `currency` CHAR(3) NOT NULL DEFAULT 'USD',
  `company_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `title_UNIQUE` (`title` ASC) VISIBLE,
  INDEX `fk_apps_company_idx` (`company_id` ASC) VISIBLE,
  CONSTRAINT `fk_apps_company`
    FOREIGN KEY (`company_id`)
    REFERENCES `play_store`.`companies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`installations` (
  `app_id` INT UNSIGNED NOT NULL,
  `device_id` INT UNSIGNED NOT NULL,
  `installed_at` DATETIME NOT NULL,
  PRIMARY KEY (`app_id`, `device_id`),
  INDEX `installations_device_id_idx` (`device_id` ASC) VISIBLE,
  CONSTRAINT `installations_app_id`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT,
  CONSTRAINT `installations_device_id`
    FOREIGN KEY (`device_id`)
    REFERENCES `play_store`.`devices` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`apps_versions` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `app_id` INT UNSIGNED NOT NULL,
  `version` VARCHAR(20) NOT NULL,
  `size_bytes` BIGINT UNSIGNED NOT NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `app_versions_app_id_version` (`app_id` ASC, `version` ASC) VISIBLE,
  CONSTRAINT `app_versions_apps_id`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`apps_discounts` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `app_id` INT UNSIGNED NOT NULL,
  `discount_price` DECIMAL(10,2) NOT NULL,
  `starts_at` DATETIME NOT NULL,
  `ends_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `app_discounts_apps_id_idx` (`app_id` ASC) VISIBLE,
  UNIQUE INDEX `uq_apps_discounts_id_app` (`id` ASC, `app_id` ASC) VISIBLE,
  CONSTRAINT `chk_apps_discounts_period` CHECK (`ends_at` > `starts_at`),
  CONSTRAINT `chk_apps_discounts_price` CHECK (`discount_price` >= 0),
  CONSTRAINT `app_discounts_apps_id`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`categories` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`apps_categories` (
  `app_id` INT UNSIGNED NOT NULL,
  `category_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`app_id`, `category_id`),
  INDEX `apps_categories_category_id_fk_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `apps_categories_app_id_fk`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT,
  CONSTRAINT `apps_categories_category_id_fk`
    FOREIGN KEY (`category_id`)
    REFERENCES `play_store`.`categories` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`reviews` (
  `account_id` INT UNSIGNED NOT NULL,
  `app_id` INT UNSIGNED NOT NULL,
  `rating` DECIMAL(2,1) NOT NULL,
  `comment` VARCHAR(350) NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`account_id`, `app_id`),
  INDEX `INDEX_app_all_ratings` (`app_id` ASC, `rating` ASC) VISIBLE,
  CONSTRAINT `chk_reviews_rating` CHECK (`rating` BETWEEN 1.0 AND 5.0),
  CONSTRAINT `reviews_account_id_accounts_fk`
    FOREIGN KEY (`account_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `reviews_app_id_apps_id_fk`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`payment_cards` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `account_id` INT UNSIGNED NOT NULL,
  `token` VARCHAR(255) NOT NULL,
  `card_brand` VARCHAR(30) NOT NULL,
  `exp_date` DATE NOT NULL,
  `last4` VARCHAR(4) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `payment_cards_account_id_fk_idx` (`account_id` ASC) VISIBLE,
  UNIQUE INDEX `token_UNIQUE` (`token` ASC) VISIBLE,
  UNIQUE INDEX `uq_payment_cards_id_account` (`id` ASC, `account_id` ASC) VISIBLE,
  CONSTRAINT `payment_cards_account_id_fk`
    FOREIGN KEY (`account_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`bills` (
  `currency` CHAR(3) NOT NULL DEFAULT 'USD',
  `amount_paid` DECIMAL(10,2) NOT NULL,
  `app_id` INT UNSIGNED NOT NULL,
  `payment_card_id` INT UNSIGNED NOT NULL,
  `paid_at` DATETIME NOT NULL,
  `discount_id` INT UNSIGNED NULL DEFAULT NULL,
  `account_id` INT UNSIGNED NOT NULL,
  INDEX `bills_app_id_apps_id_fk_idx` (`app_id` ASC) VISIBLE,
  PRIMARY KEY (`account_id`, `app_id`),
  INDEX `fk_bills_payment_card_idx` (`payment_card_id` ASC, `account_id` ASC) VISIBLE,
  INDEX `fk_bills_discount_idx` (`discount_id` ASC, `app_id` ASC) VISIBLE,
  CONSTRAINT `bills_app_id_apps_id_fk`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `bills_account_id_accounts_id_fk`
    FOREIGN KEY (`account_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_bills_payment_card`
    FOREIGN KEY (`payment_card_id` , `account_id`)
    REFERENCES `play_store`.`payment_cards` (`id` , `account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_bills_discount`
    FOREIGN KEY (`discount_id` , `app_id`)
    REFERENCES `play_store`.`apps_discounts` (`id` , `app_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `play_store`.`library` (
  `app_id` INT UNSIGNED NOT NULL,
  `account_id` INT UNSIGNED NOT NULL,
  `app_data` JSON NULL,
  `last_opened_at` DATETIME NULL,
  PRIMARY KEY (`app_id`, `account_id`),
  INDEX `library_account_id_accounts_id_fk_idx` (`account_id` ASC) VISIBLE,
  CONSTRAINT `library_app_id_apps_id_fk`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `library_account_id_accounts_id_fk`
    FOREIGN KEY (`account_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
