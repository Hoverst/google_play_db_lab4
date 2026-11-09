"""DAO for the devices table."""

from my_project import db
from my_project.auth.domain.devices import Device


def find_all():
    """Return all device records."""
    return Device.query.all()


def find_by_id(id):
    """Return a single device by primary key."""
    return Device.query.get(id)


def create(data):
    """Create a new device from a dict and persist it."""
    instance = Device(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    """Update an existing device instance with values from a dict."""
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    """Delete a device instance from the database."""
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
