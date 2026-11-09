"""Controller for devices CRUD operations and relationship endpoints."""

from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.devices import Device
from my_project.auth.service import devices_service


def get_all():
    """Return all devices."""
    result = devices_service.get_all()
    return jsonify(result), 200


def get_by_id(device_id):
    """Return a single device by ID."""
    result = devices_service.get_by_id(device_id)
    return jsonify(result), 200


def create():
    """Create a new device."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = devices_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(device_id):
    """Update an existing device."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = devices_service.update(device_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(device_id):
    """Delete a device by ID."""
    try:
        devices_service.delete(device_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


# --- Relationship endpoints ---

def get_installations(device_id):
    """Return all installations for a given device."""
    device = Device.query.get(device_id)
    if device is None:
        abort(404)
    return jsonify([item.to_dict() for item in device.installations]), 200


def get_accounts(device_id):
    """Return all accounts for a given device (M:M through accounts_devices)."""
    device = Device.query.get(device_id)
    if device is None:
        abort(404)
    return jsonify([item.to_dict() for item in device.accounts]), 200
