"""DAO for the apps_discounts table."""

from my_project import db
from my_project.auth.domain.apps_discounts import AppDiscount


def find_all():
    """Return all app discount records."""
    return AppDiscount.query.all()


def find_by_id(id):
    """Return a single app discount by primary key."""
    return AppDiscount.query.get(id)


def create(data):
    """Create a new app discount from a dict and persist it."""
    instance = AppDiscount(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing app discount instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete an app discount instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
