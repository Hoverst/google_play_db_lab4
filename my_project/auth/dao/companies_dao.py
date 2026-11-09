"""DAO for the companies table."""

from my_project import db
from my_project.auth.domain.companies import Company


def find_all():
    """Return all company records."""
    return Company.query.all()


def find_by_id(id):
    """Return a single company by primary key."""
    return Company.query.get(id)


def create(data):
    """Create a new company from a dict and persist it."""
    instance = Company(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing company instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete a company instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
