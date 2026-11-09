"""DAO for the payment_cards table."""

from my_project import db
from my_project.auth.domain.payment_cards import PaymentCard


def find_all():
    """Return all payment card records."""
    return PaymentCard.query.all()


def find_by_id(id):
    """Return a single payment card by primary key."""
    return PaymentCard.query.get(id)


def create(data):
    """Create a new payment card from a dict and persist it."""
    instance = PaymentCard(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing payment card instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete a payment card instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
