"""DAO for the bills table (composite PK: account_id, app_id)."""

from my_project import db
from my_project.auth.domain.bills import Bill


def find_all():
    """Return all bill records."""
    return Bill.query.all()


def find_by_id(account_id, app_id):
    """Return a single bill record by composite primary key."""
    return Bill.query.get((account_id, app_id))


def create(data):
    """Create a new bill record from a dict and persist it."""
    instance = Bill(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing bill instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete a bill instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
