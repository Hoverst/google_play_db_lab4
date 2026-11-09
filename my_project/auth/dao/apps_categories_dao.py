"""DAO for the apps_categories table (composite PK: app_id, category_id)."""

from my_project import db
from my_project.auth.domain.apps_categories import AppCategory


def find_all():
    """Return all app-category records."""
    return AppCategory.query.all()


def find_by_id(app_id, category_id):
    """Return a single app-category record by composite primary key."""
    return AppCategory.query.get((app_id, category_id))


def create(data):
    """Create a new app-category record from a dict and persist it."""
    instance = AppCategory(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing app-category instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete an app-category instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
