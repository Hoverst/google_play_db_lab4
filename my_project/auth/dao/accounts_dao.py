"""DAO for the accounts table."""

from my_project import db
from my_project.auth.domain.accounts import Account


def find_all():
    """Return all account records."""
    return Account.query.all()


def find_by_id(id):
    """Return a single account by primary key."""
    return Account.query.get(id)


def create(data):
    """Create a new account from a dict and persist it."""
    instance = Account(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing account instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete an account instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
