from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.devices import Device
from my_project.auth.service import devices_service

def get_all():
    result = devices_service.get_all()
    return jsonify(result), 200

def get_by_id(device_id):
    result = devices_service.get_by_id(device_id)
    return jsonify(result), 200

def create():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = devices_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def update(device_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = devices_service.update(device_id, data, partial=False)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def patch(device_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = devices_service.update(device_id, data, partial=True)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def delete(device_id):
    try:
        devices_service.delete(device_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def get_installations(device_id):
    device = Device.query.get(device_id)
    if device is None:
        abort(404)
    return jsonify([item.to_dict() for item in device.installations]), 200

def get_accounts(device_id):
    device = Device.query.get(device_id)
    if device is None:
        abort(404)
    return jsonify([item.to_dict() for item in device.accounts]), 200
