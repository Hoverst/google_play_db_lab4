# Play Store API

Flask + SQLAlchemy REST API for the MySQL `play_store` schema (Google Play–like store).

## Architecture

```
Postman / Client
  → Route
  → Controller
  → DTO (validation)
  → Service (business rules)
  → DAO
  → MySQL
```

## Domain

Tables: `accounts` (soft delete), `devices`, `accounts_devices` (M:N), `companies`, `apps`, `categories`, `apps_categories` (M:N), `apps_versions`, `installations`, `library`, `reviews`.

Password storage: unsalted SHA-256 hex (`hashlib.sha256`), matching MySQL `SHA2(password, 256)` in `seed.sql`. Responses never include `password_hash`.

## Configure

1. Copy `config/app.example.yml` → `config/app.yml` and set your MySQL credentials.
2. Create and seed the database (script is the source of truth):

```bash
mysql -u root -p < data.sql
mysql -u root -p < seed.sql
```

## Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Base URL: `http://127.0.0.1:5000`

## Endpoints (CRUD)

| Resource | Base |
|---|---|
| accounts | `/accounts` |
| devices | `/devices` |
| companies | `/companies` |
| categories | `/categories` |
| apps | `/apps` |
| apps_versions | `/apps_versions` |
| installations | `/installations` |
| library | `/library` |
| reviews | `/reviews` |

Methods: `GET` list, `GET /<id>`, `POST`, `PUT` (full), `PATCH` (partial), `DELETE`.

### Delete semantics

- `DELETE /accounts/<id>` — **soft delete**: sets `deleted_at` (row kept); the account disappears from `GET /accounts` and returns `404`. Every app owned by that developer's company becomes `unpublished` (apps already `suspended` keep that state).
- `DELETE /apps/<id>` — **hard delete** (`204`) when the app has no versions, library entries or reviews; otherwise **soft delete** by setting `status = 'unpublished'` (`200` with the app JSON). Idempotent, and never downgrades `suspended`.
- Other resources delete physically and return `409` when related rows block the delete.

### Relationships

- `GET/POST /accounts/<id>/devices`, `DELETE /accounts/<id>/devices/<device_id>`
- `GET /devices/<id>/accounts`
- `GET/POST /apps/<id>/categories`, `DELETE /apps/<id>/categories/<category_id>`
- `GET /categories/<id>/apps`
- `GET /companies/<id>/apps`
- `GET /apps/<id>/versions`
- `GET /accounts/<id>/library`, `GET /apps/<id>/library`
- `GET /apps/<id>/reviews`
- `GET /accounts/<id>/companies`
- `GET /devices/<id>/installations`, `GET /apps_versions/<id>/installations`

## PUT vs PATCH

- **PUT**: all writable fields required.
- **PATCH**: at least one writable field; unknown fields → `400`.

## Tests

```bash
pytest
```

## Postman

Import/open the collection postman_collection.json
