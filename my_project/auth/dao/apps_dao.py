"""DAO for the apps table."""

from my_project import db
from my_project.auth.domain.apps import App


def find_all():
    """Return all app records."""
    return App.query.all()


def find_by_id(id):
    """Return a single app by primary key."""
    return App.query.get(id)


def create(data):
    """Create a new app from a dict and persist it."""
    instance = App(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing app instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete an app instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
