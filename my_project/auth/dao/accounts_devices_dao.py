"""DAO for the accounts_devices table (composite PK: account_id, device_id)."""

from my_project import db
from my_project.auth.domain.accounts_devices import AccountDevice


def find_all():
    """Return all account-device records."""
    return AccountDevice.query.all()


def find_by_id(account_id, device_id):
    """Return a single account-device record by composite primary key."""
    return AccountDevice.query.get((account_id, device_id))


def create(data):
    """Create a new account-device record from a dict and persist it."""
    instance = AccountDevice(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing account-device instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete an account-device instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
