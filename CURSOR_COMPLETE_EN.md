# Cursor Agent Task: AUDIT and COMPLETE an unfinished Flask + MySQL Back-End (Lab 4)

You are working in agent mode. A previous AI agent started this project and stopped before finishing. Your job is to **find out what is missing or broken and complete it**, not to start over. Do everything on your own without asking clarifying questions. If something is ambiguous, pick a reasonable option and record it in `README.md` (section "Assumptions").

---

## 0. Rules of engagement

- **Do not rewrite or delete working code.** Reuse existing files, naming style and patterns. Only add what is missing and fix what is broken.
- The database **already exists** on the local MySQL server with its data. Never run `DROP`, `TRUNCATE`, `CREATE DATABASE`, `db.create_all()` or `db.drop_all()`, and never change the schema. If you find `db.create_all()` / `drop_all()` in the code, remove it.
- Take table names, columns, types, primary and foreign keys ONLY from the schema (section 2). Do not invent anything.
- I will enter the MySQL password myself in `config/app.yml`. Do not guess or ask for it. Do not commit a real password.
- Code comments and `README.md` in English. Identifiers (variables, classes, files, URLs) in English.
- Do NOT run `git push` and do not add a remote.

## 1. What I already know about the current state

Project root is `app/`. The root currently shows only: `config/`, `my_project/`, `tests/`, `.gitignore`, `app.py`, `setup.py`.

Known to be **missing from the root**: `requirements.txt`, `README.md`, `postman_collection.json`, `data.sql`. I have not looked inside the folders, so they may be incomplete too. Verify everything in step 3.

## 2. Database SQL schema (source of truth)

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

## 3. Step 1: Audit (do this first, before changing anything)

Inspect the whole project (including hidden files) and run `python -m compileall .` to catch syntax errors. Then print an **audit table in the chat** with one row per item and a status of `OK`, `MISSING`, `EMPTY/STUB` (file exists but has only `pass`, `TODO` or no real logic) or `BROKEN` (syntax/import error or wrong behavior):

1. Project root files: `requirements.txt`, `data.sql`, `README.md`, `postman_collection.json`, `.gitignore`, `setup.py`, `app.py`, `config/app.yml`.
2. Folders and `__init__.py` presence: `my_project/`, `my_project/auth/{controller,dao,domain,route,service}`, `my_project/ui`, `my_project/utils`, `tests/`.
3. `my_project/__init__.py`: `create_app()` reads `config/app.yml`, builds the `mysql+pymysql://` URL, declares `db = SQLAlchemy()` at module level, registers all blueprints (imports inside `create_app`, no circular imports).
4. **Per table in the schema**, check each of the five files: `domain/<name>.py`, `dao/<name>_dao.py`, `service/<name>_service.py`, `controller/<name>_controller.py`, `route/<name>_route.py`, and whether the blueprint is registered.
5. Relationships: M:1 endpoints for every foreign key, M:M endpoints (both directions) for every junction table.
6. Central error handling returning JSON `{"error": "..."}`.
7. Tests in `tests/`.
8. Git: whether a repository exists (`.git`) and whether there is at least one commit.

## 4. Step 2: Complete everything that is MISSING, EMPTY/STUB or BROKEN

Fix in this order, following the target specification below.

### 4.1 Target specification

**Technologies:** Python 3.10+, `flask`, `flask-sqlalchemy` 3.x, `pymysql`, `pyyaml`, `cryptography`, `pytest`. Use a `venv` in the project root if there is none.

**Configuration:** `config/app.yml`

```yaml
db:
  user: root
  password: your_password   # the user will replace this
  host: localhost
  port: 3306
  name: play_store          # real database name from the schema
```

The config path must be built from the project root so the app works from any launch directory. If the existing file contains a real-looking password, replace it with the placeholder `your_password`.

**Layers (per table):**
- **domain**: SQLAlchemy model accurately mapping columns, types, relationships. `to_dict()` returns all columns (this is the DTO); convert `Decimal`, `datetime`, `date` to JSON-safe values. JSON keys equal column names.
- **dao**: `find_all`, `find_by_id`, `create`, `update`, `delete` using `db.session` with `commit` and `rollback` on error.
- **service**: thin layer; checks the record exists (else "not found"), required fields are present, then calls the dao.
- **controller**: reads `request.get_json()`, calls the service, returns `jsonify(...)` with status codes: 200 (read, update), 201 (create), 204 (delete), 400 (bad request), 404 (not found), 409 (integrity violation such as `IntegrityError`).
- **route**: `Blueprint` with `url_prefix="/<table_name>"`:

| Method | URL | Action |
|---|---|---|
| GET | `/<table>` | list all |
| GET | `/<table>/<id>` | one record |
| POST | `/<table>` | create |
| PUT | `/<table>/<id>` | update |
| DELETE | `/<table>/<id>` | delete |

For M:M junction tables and tables with a composite primary key use `/<table>/<id1>/<id2>`; they need full CRUD too.

Never expose stack traces; handle errors centrally (for example `utils/errors.py` with `@app.errorhandler`).

**Relationships (required by the assignment):**
1. **M:1**: for every foreign key, an endpoint on the "one" side returning all dependent records (example: `GET /companies/<id>/apps`), plus the matching `db.relationship(...)`.
2. **M:M**: for every junction table, endpoints in both directions (example: `GET /accounts/<id>/devices` and `GET /devices/<id>/accounts`; apps and categories likewise).

All of them return an array of DTOs and 404 if the parent record does not exist.

### 4.2 Files that are known to be missing: create them

- `requirements.txt`: install the libraries into the venv, then `pip freeze > requirements.txt`.
- `data.sql`: the table schema (from section 2).
- `postman_collection.json`: **Postman Collection v2.1**, importable as is. Variable `baseUrl = http://127.0.0.1:5000`; one folder per table (GET all, GET by id, POST with an example JSON body matching the columns, PUT, DELETE); separate folders "M:1 relationships" and "M:M relationships" with every endpoint above; POST/PUT have header `Content-Type: application/json` and a `raw` JSON body.
- `README.md` in English: what the project is and which database it uses; how to run it (create venv, `pip install -r requirements.txt`, put the password into `config/app.yml`, `python app.py`); table of all endpoints; how to import the Postman collection; layer diagram Postman → route → controller → service → dao → MySQL; "Assumptions" section.
- `tests/test_smoke.py` (if missing or empty): `pytest` + Flask test client; for every table check that `GET /<table>` returns 200 and a list. Read-only, tests must not modify data.
- `.gitignore`: make sure it contains `venv/`, `.idea/`, `.vscode/`, `__pycache__/`, `*.pyc`, `.pytest_cache/` (add only what is missing).

### 4.3 Git

If there is no repository, run `git init`. Then `git add .` and commit with the message `Lab 4: Flask back-end` (if a commit with sensible history already exists, make a new commit with the message `Complete Lab 4 back-end`). No push, no remote.

## 5. Step 3: Verify

Run and fix anything that fails:
1. `python -m compileall .` passes and `python app.py` starts without errors or import warnings.
2. If MySQL is reachable from the terminal, verify with `curl` or tests: `GET` on several tables and on both relationship types returns valid JSON. To test POST/PUT/DELETE, create a test record and delete it right away; never touch existing data. If MySQL is not reachable from the terminal, do not invent results: say honestly that it was not verified.
3. `pytest` passes (or explain exactly why it cannot).
4. Every table in the schema has all five files, a registered blueprint and routes; every foreign key has its M:1 endpoint and every junction table has both M:M endpoints.
5. The repository contains no real password.

## 6. Final response

Output briefly: the audit table (before) and what you changed (after), the list of tables and relationship endpoints, what was verified and what was not, and what I must do manually (enter the password in `config/app.yml`, run the app, import the collection into Postman, push to GitHub).
