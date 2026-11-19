import uuid
import pytest
from my_project import create_app
from my_project.utils.password import hash_password


@pytest.fixture(scope="module")
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def _uid():
    return uuid.uuid4().hex[:10]


def test_password_hash_matches_sha2():
    expected = __import__("hashlib").sha256(b"demo_password_1").hexdigest()
    assert hash_password("demo_password_1") == expected
    assert len(expected) == 64


def test_account_crud_and_soft_delete(client):
    email = f"tmp_{_uid()}@example.com"
    created = client.post(
        "/accounts",
        json={"email": email, "password": "password123", "name": "Temp User"},
    )
    assert created.status_code == 201, created.get_json()
    body = created.get_json()
    assert "password_hash" not in body
    account_id = body["id"]

    assert client.get(f"/accounts/{account_id}").status_code == 200

    put = client.put(
        f"/accounts/{account_id}",
        json={"email": email, "password": "password456", "name": "Renamed"},
    )
    assert put.status_code == 200
    assert put.get_json()["name"] == "Renamed"

    patch = client.patch(f"/accounts/{account_id}", json={"name": "Patched"})
    assert patch.status_code == 200
    assert patch.get_json()["name"] == "Patched"

    assert client.delete(f"/accounts/{account_id}").status_code == 204
    assert client.get(f"/accounts/{account_id}").status_code == 404


def test_duplicate_email_409(client):
    email = f"dup_{_uid()}@example.com"
    assert client.post(
        "/accounts", json={"email": email, "password": "password123", "name": "A"}
    ).status_code == 201
    again = client.post(
        "/accounts", json={"email": email, "password": "password123", "name": "B"}
    )
    assert again.status_code == 409


def test_category_put_patch_validation(client):
    name = f"cat_{_uid()}"
    created = client.post("/categories", json={"name": name})
    assert created.status_code == 201
    cat_id = created.get_json()["id"]

    assert client.put(f"/categories/{cat_id}", json={}).status_code == 400
    assert client.put(f"/categories/{cat_id}", json={"name": name, "x": 1}).status_code == 400
    assert client.patch(f"/categories/{cat_id}", json={}).status_code == 400
    assert client.put("/categories/2147483646", json={"name": "x"}).status_code == 404

    new_name = f"cat2_{_uid()}"
    assert client.put(f"/categories/{cat_id}", json={"name": new_name}).status_code == 200
    assert client.patch(f"/categories/{cat_id}", json={"name": f"cat3_{_uid()}"}).status_code == 200
    assert client.delete(f"/categories/{cat_id}").status_code == 204


def test_review_requires_library(client):
    accounts = client.get("/accounts").get_json()
    apps = client.get("/apps").get_json()
    assert accounts and apps
    # Find an account/app pair with no library entry — use new account
    email = f"norev_{_uid()}@example.com"
    acc = client.post(
        "/accounts", json={"email": email, "password": "password123", "name": "No Lib"}
    ).get_json()
    app_id = apps[0]["id"]
    resp = client.post(
        "/reviews",
        json={"account_id": acc["id"], "app_id": app_id, "rating": 4.5, "comment": "x"},
    )
    assert resp.status_code == 409
    client.delete(f"/accounts/{acc['id']}")


def test_mm_accounts_devices(client):
    email = f"devlink_{_uid()}@example.com"
    acc = client.post(
        "/accounts", json={"email": email, "password": "password123", "name": "Link"}
    ).get_json()
    device = client.post(
        "/devices", json={"model": f"M-{_uid()}", "os_version": "99"}
    ).get_json()

    attach = client.post(f"/accounts/{acc['id']}/devices", json={"device_id": device["id"]})
    assert attach.status_code == 201

    listed = client.get(f"/accounts/{acc['id']}/devices")
    assert listed.status_code == 200
    assert any(d["id"] == device["id"] for d in listed.get_json())

    assert client.delete(f"/accounts/{acc['id']}/devices/{device['id']}").status_code == 204
    client.delete(f"/devices/{device['id']}")
    client.delete(f"/accounts/{acc['id']}")


def test_rating_out_of_range(client):
    libs = client.get("/library").get_json()
    if not libs:
        pytest.skip("no library seed rows")
    entry = libs[0]
    resp = client.post(
        "/reviews",
        json={
            "account_id": entry["account_id"],
            "app_id": entry["app_id"],
            "rating": 5.5,
            "comment": "bad",
        },
    )
    # may be 400 validation or 409 if review already exists for this pair
    assert resp.status_code in (400, 409)


def _make_developer(client, status=None):
    """Create an account + company + one app; return (account, company, app)."""
    uid = _uid()
    acc = client.post(
        "/accounts",
        json={"email": f"soft_{uid}@example.com", "password": "password123", "name": "Soft"},
    ).get_json()
    company = client.post(
        "/companies",
        json={
            "company_name": f"Soft Co {uid}",
            "contact_email": f"soft_{uid}@example.com",
            "developer_id": acc["id"],
        },
    ).get_json()
    app_body = {
        "title": f"Soft App {uid}",
        "package_name": f"com.soft.{uid}",
        "caption": "soft delete test",
        "company_id": company["id"],
    }
    if status is not None:
        app_body["status"] = status
    app = client.post("/apps", json=app_body).get_json()
    return acc, company, app


def test_app_delete_soft_deletes_when_it_has_dependents(client):
    acc, company, app = _make_developer(client)
    version = client.post(
        "/apps_versions",
        json={"app_id": app["id"], "version": "1.0.0", "size_bytes": 1024},
    )
    assert version.status_code == 201
    version_id = version.get_json()["id"]

    deleted = client.delete(f"/apps/{app['id']}")
    assert deleted.status_code == 200
    assert deleted.get_json()["status"] == "unpublished"

    fetched = client.get(f"/apps/{app['id']}")
    assert fetched.status_code == 200
    assert fetched.get_json()["status"] == "unpublished"

    # Deleting again is idempotent while dependents exist.
    again = client.delete(f"/apps/{app['id']}")
    assert again.status_code == 200
    assert again.get_json()["status"] == "unpublished"

    # Remove the dependent, then the app can be hard-deleted.
    assert client.delete(f"/apps_versions/{version_id}").status_code == 204
    assert client.delete(f"/apps/{app['id']}").status_code == 204
    assert client.get(f"/apps/{app['id']}").status_code == 404

    client.delete(f"/companies/{company['id']}")
    client.delete(f"/accounts/{acc['id']}")


def test_app_delete_hard_deletes_without_dependents(client):
    acc, company, app = _make_developer(client)

    assert client.delete(f"/apps/{app['id']}").status_code == 204
    assert client.get(f"/apps/{app['id']}").status_code == 404

    client.delete(f"/companies/{company['id']}")
    client.delete(f"/accounts/{acc['id']}")


def test_account_soft_delete_unpublishes_developer_apps(client):
    acc, company, published = _make_developer(client)
    suspended = client.post(
        "/apps",
        json={
            "title": f"Suspended App {_uid()}",
            "package_name": f"com.suspended.{_uid()}",
            "company_id": company["id"],
            "status": "suspended",
        },
    ).get_json()

    assert client.delete(f"/accounts/{acc['id']}").status_code == 204
    assert client.get(f"/accounts/{acc['id']}").status_code == 404

    published_after = client.get(f"/apps/{published['id']}")
    assert published_after.status_code == 200
    assert published_after.get_json()["status"] == "unpublished"

    # Moderation state is not downgraded.
    suspended_after = client.get(f"/apps/{suspended['id']}")
    assert suspended_after.status_code == 200
    assert suspended_after.get_json()["status"] == "suspended"

    client.delete(f"/apps/{published['id']}")
    client.delete(f"/apps/{suspended['id']}")
    client.delete(f"/companies/{company['id']}")

