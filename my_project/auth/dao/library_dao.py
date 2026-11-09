"""DAO for the library table (composite PK: app_id, account_id)."""

from my_project import db
from my_project.auth.domain.library import Library


def find_all():
    """Return all library records."""
    return Library.query.all()


def find_by_id(app_id, account_id):
    """Return a single library record by composite primary key."""
    return Library.query.get((app_id, account_id))


def create(data):
    """Create a new library record from a dict and persist it."""
    instance = Library(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing library instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete a library instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
