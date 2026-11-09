# Play Store API (Lab 4)

Flask + MySQL back-end for the `play_store` database. The API exposes full CRUD for every table and relationship endpoints for foreign keys (M:1) and junction tables (M:M).

## Stack

- Python 3.10+
- Flask, Flask-SQLAlchemy 3.x, PyMySQL, PyYAML, cryptography, pytest
- MySQL database: `play_store` (schema in `data.sql`)

## How to run

1. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Put your MySQL password into `config/app.yml` (replace `your_password`).

4. Start the server:

```bash
python app.py
```

The API listens on `http://127.0.0.1:5000`.

## Layer diagram

```
Postman / HTTP client
        ↓
      route
        ↓
    controller
        ↓
      service
        ↓
        dao
        ↓
   MySQL (play_store)
```

## Endpoints (CRUD)

| Table | Base URL | ID style |
|---|---|---|
| accounts | `/accounts` | `/<id>` |
| devices | `/devices` | `/<id>` |
| accounts_devices | `/accounts_devices` | `/<account_id>/<device_id>` |
| companies | `/companies` | `/<id>` |
| apps | `/apps` | `/<id>` |
| installations | `/installations` | `/<app_id>/<device_id>` |
| apps_versions | `/apps_versions` | `/<id>` |
| apps_discounts | `/apps_discounts` | `/<id>` |
| categories | `/categories` | `/<id>` |
| apps_categories | `/apps_categories` | `/<app_id>/<category_id>` |
| reviews | `/reviews` | `/<account_id>/<app_id>` |
| payment_cards | `/payment_cards` | `/<id>` |
| bills | `/bills` | `/<account_id>/<app_id>` |
| library | `/library` | `/<app_id>/<account_id>` |

Methods: `GET` list, `GET` one, `POST` create (201), `PUT` update (200), `DELETE` (204).

### M:1 relationship endpoints

- `GET /accounts/<id>/companies`
- `GET /accounts/<id>/payment_cards`
- `GET /accounts/<id>/reviews`
- `GET /accounts/<id>/bills`
- `GET /accounts/<id>/library`
- `GET /companies/<id>/apps`
- `GET /apps/<id>/versions`
- `GET /apps/<id>/discounts`
- `GET /apps/<id>/reviews`
- `GET /apps/<id>/bills`
- `GET /apps/<id>/library`
- `GET /apps/<id>/installations`
- `GET /devices/<id>/installations`
- `GET /payment_cards/<id>/bills`
- `GET /apps_discounts/<id>/bills`

### M:M relationship endpoints

- `GET /accounts/<id>/devices`
- `GET /devices/<id>/accounts`
- `GET /apps/<id>/categories`
- `GET /categories/<id>/apps`

## Postman

1. Open Postman → Import → choose `postman_collection.json`.
2. Collection variable `baseUrl` defaults to `http://127.0.0.1:5000`.
3. Folders: one per table (CRUD), plus **M:1 relationships** and **M:M relationships**.

## Tests

```bash
pytest
```

Smoke tests only call `GET /<table>` and must not modify data. MySQL must be reachable with the password from `config/app.yml`.

## Assumptions

- The `play_store` database and its data already exist locally; the app never creates or drops the schema.
- `config/app.yml` password is entered by the developer; the committed value is the placeholder `your_password`.
- Composite primary keys use `/<id1>/<id2>` paths in the same column order as the schema PK.
- Relationship endpoints return JSON arrays of DTO objects and `404` when the parent row is missing.
- `installations` is treated as an association entity with its own CRUD plus M:1 lists from `apps` and `devices` (it is not a pure M:M without payload).
- Integer column types in SQLAlchemy map to MySQL `INT UNSIGNED` columns already present in the database.
