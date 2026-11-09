"""DAO for the reviews table (composite PK: account_id, app_id)."""

from my_project import db
from my_project.auth.domain.reviews import Review


def find_all():
    """Return all review records."""
    return Review.query.all()


def find_by_id(account_id, app_id):
    """Return a single review record by composite primary key."""
    return Review.query.get((account_id, app_id))


def create(data):
    """Create a new review record from a dict and persist it."""
    instance = Review(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing review instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete a review instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
