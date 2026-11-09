"""DAO for the categories table."""

from my_project import db
from my_project.auth.domain.categories import Category


def find_all():
    """Return all category records."""
    return Category.query.all()


def find_by_id(id):
    """Return a single category by primary key."""
    return Category.query.get(id)


def create(data):
    """Create a new category from a dict and persist it."""
    instance = Category(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing category instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete a category instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
