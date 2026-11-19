from flask import request, jsonify, abort
from my_project.auth.dto import devices_dto
from my_project.auth.service import devices_service


def get_all():
    return jsonify(devices_service.get_all()), 200


def get_by_id(device_id):
    return jsonify(devices_service.get_by_id(device_id)), 200


def create():
    data = devices_dto.parse_create(request.get_json(silent=True))
    return jsonify(devices_service.create(data)), 201


def update(device_id):
    data = devices_dto.parse_put(request.get_json(silent=True))
    return jsonify(devices_service.update(device_id, data, partial=False)), 200


def patch(device_id):
    data = devices_dto.parse_patch(request.get_json(silent=True))
    return jsonify(devices_service.update(device_id, data, partial=True)), 200


def delete(device_id):
    devices_service.delete(device_id)
    return "", 204


def get_accounts(device_id):
    from my_project.auth.service import accounts_devices_service
    return jsonify(accounts_devices_service.list_accounts(device_id)), 200


def get_installations(device_id):
    from my_project.auth.dao import devices_dao
    device = devices_dao.find_by_id(device_id)
    if device is None:
        abort(404)
    return jsonify([i.to_dict() for i in device.installations]), 200
