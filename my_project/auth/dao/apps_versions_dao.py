"""DAO for the apps_versions table."""

from my_project import db
from my_project.auth.domain.apps_versions import AppVersion


def find_all():
    """Return all app version records."""
    return AppVersion.query.all()


def find_by_id(id):
    """Return a single app version by primary key."""
    return AppVersion.query.get(id)


def create(data):
    """Create a new app version from a dict and persist it."""
    instance = AppVersion(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing app version instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete an app version instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
