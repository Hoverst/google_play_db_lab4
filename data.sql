SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

SET NAMES utf8mb4;

DROP SCHEMA IF EXISTS play_store;
CREATE SCHEMA play_store;

CREATE TABLE `play_store`.`accounts` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `name` VARCHAR(70) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_accounts_email` (`email` ASC) VISIBLE,
  INDEX `idx_accounts_name` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`devices` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `model` VARCHAR(45) NOT NULL,
  `os_version` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_devices_model_os_version` (`model` ASC, `os_version` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`accounts_devices` (
  `account_id` INT UNSIGNED NOT NULL,
  `device_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`account_id`, `device_id`),
  INDEX `idx_accounts_devices_device_id` (`device_id` ASC) VISIBLE,
  CONSTRAINT `fk_accounts_devices_account_id`
    FOREIGN KEY (`account_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_accounts_devices_device_id`
    FOREIGN KEY (`device_id`)
    REFERENCES `play_store`.`devices` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`companies` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `company_name` VARCHAR(60) NOT NULL,
  `contact_email` VARCHAR(255) NULL DEFAULT NULL,
  `developer_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_companies_company_name` (`company_name` ASC) VISIBLE,
  UNIQUE INDEX `uq_companies_developer_id` (`developer_id` ASC) VISIBLE,
  CONSTRAINT `fk_companies_developer_id`
    FOREIGN KEY (`developer_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`apps` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(80) NOT NULL,
  `package_name` VARCHAR(150) NOT NULL,
  `caption` VARCHAR(600) NULL DEFAULT NULL,
  `company_id` INT UNSIGNED NOT NULL,
  `status` ENUM('published', 'unpublished', 'suspended') NOT NULL DEFAULT 'published',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_apps_package_name` (`package_name` ASC) VISIBLE,
  INDEX `idx_apps_company_id` (`company_id` ASC) VISIBLE,
  CONSTRAINT `fk_apps_company_id`
    FOREIGN KEY (`company_id`)
    REFERENCES `play_store`.`companies` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`categories` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_categories_name` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`apps_categories` (
  `app_id` INT UNSIGNED NOT NULL,
  `category_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`app_id`, `category_id`),
  INDEX `idx_apps_categories_category_id` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_apps_categories_app_id`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_apps_categories_category_id`
    FOREIGN KEY (`category_id`)
    REFERENCES `play_store`.`categories` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`apps_versions` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `app_id` INT UNSIGNED NOT NULL,
  `version` VARCHAR(20) NOT NULL,
  `size_bytes` BIGINT UNSIGNED NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_apps_versions_app_id_version` (`app_id` ASC, `version` ASC) VISIBLE,
  CONSTRAINT `fk_apps_versions_app_id`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`installations` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `device_id` INT UNSIGNED NOT NULL,
  `app_version_id` INT UNSIGNED NOT NULL,
  `installed_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_installations_device_id_app_version_id` (`device_id` ASC, `app_version_id` ASC) VISIBLE,
  INDEX `idx_installations_app_version_id_device_id` (`app_version_id` ASC, `device_id` ASC) VISIBLE,
  INDEX `idx_installations_installed_at` (`installed_at` ASC) VISIBLE,
  CONSTRAINT `fk_installations_app_version_id`
    FOREIGN KEY (`app_version_id`)
    REFERENCES `play_store`.`apps_versions` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_installations_device_id`
    FOREIGN KEY (`device_id`)
    REFERENCES `play_store`.`devices` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`library` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `app_id` INT UNSIGNED NOT NULL,
  `account_id` INT UNSIGNED NOT NULL,
  `last_opened_at` DATETIME NULL DEFAULT NULL,
  `added_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data_ref` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_library_account_id_app_id` (`account_id` ASC, `app_id` ASC) VISIBLE,
  INDEX `idx_library_app_id` (`app_id` ASC) VISIBLE,
  CONSTRAINT `fk_library_account_id`
    FOREIGN KEY (`account_id`)
    REFERENCES `play_store`.`accounts` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_library_app_id`
    FOREIGN KEY (`app_id`)
    REFERENCES `play_store`.`apps` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `play_store`.`reviews` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `account_id` INT UNSIGNED NOT NULL,
  `app_id` INT UNSIGNED NOT NULL,
  `rating` DECIMAL(2,1) NOT NULL,
  `comment` VARCHAR(350) NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_reviews_account_id_app_id` (`account_id` ASC, `app_id` ASC) VISIBLE,
  INDEX `idx_reviews_app_id_rating` (`app_id` ASC, `rating` ASC) VISIBLE,
  CONSTRAINT `fk_reviews_library`
    FOREIGN KEY (`account_id` , `app_id`)
    REFERENCES `play_store`.`library` (`account_id` , `app_id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `chk_reviews_rating`
    CHECK (`rating` BETWEEN 0.0 AND 5.0))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;