"""DAO for the installations table (composite PK: app_id, device_id)."""

from my_project import db
from my_project.auth.domain.installations import Installation


def find_all():
    """Return all installation records."""
    return Installation.query.all()


def find_by_id(app_id, device_id):
    """Return a single installation record by composite primary key."""
    return Installation.query.get((app_id, device_id))


def create(data):
    """Create a new installation record from a dict and persist it."""
    instance = Installation(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing installation instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete an installation instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
