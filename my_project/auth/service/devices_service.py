"""Service layer for the devices table."""

from flask import abort
from my_project.auth.dao import devices_dao


def get_all():
    """Return all devices as a list of dicts."""
    return [instance.to_dict() for instance in devices_dao.find_all()]


def get_by_id(id):
    """Return a single device dict by primary key, or abort 404."""
    instance = devices_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new device, and return its dict."""
    required_fields = ['model', 'os_version']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = devices_dao.create(data)
    return instance.to_dict()


def update(id, data):
    """Update an existing device by id and return its dict, or abort 404."""
    instance = devices_dao.find_by_id(id)
    if instance is None:
        abort(404)
    instance = devices_dao.update(instance, data)
    return instance.to_dict()


def delete(id):
    """Delete a device by id, or abort 404."""
    instance = devices_dao.find_by_id(id)
    if instance is None:
        abort(404)
    devices_dao.delete(instance)
