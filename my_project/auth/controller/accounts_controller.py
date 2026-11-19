from flask import request, jsonify, abort
from my_project.auth.dto import accounts_dto
from my_project.auth.service import accounts_service


def get_all():
    return jsonify(accounts_service.get_all()), 200


def get_by_id(account_id):
    return jsonify(accounts_service.get_by_id(account_id)), 200


def create():
    data = accounts_dto.parse_create(request.get_json(silent=True))
    return jsonify(accounts_service.create(data)), 201


def update(account_id):
    data = accounts_dto.parse_put(request.get_json(silent=True))
    return jsonify(accounts_service.update(account_id, data, partial=False)), 200


def patch(account_id):
    data = accounts_dto.parse_patch(request.get_json(silent=True))
    return jsonify(accounts_service.update(account_id, data, partial=True)), 200


def delete(account_id):
    accounts_service.delete(account_id)
    return "", 204


def get_devices(account_id):
    from my_project.auth.service import accounts_devices_service
    return jsonify(accounts_devices_service.list_devices(account_id)), 200


def attach_device(account_id):
    from my_project.auth.service import accounts_devices_service
    from my_project.auth.dto._common import require_dict, as_pos_int
    data = require_dict(request.get_json(silent=True))
    device_id = as_pos_int(data, "device_id")
    return jsonify(accounts_devices_service.attach(account_id, device_id)), 201


def detach_device(account_id, device_id):
    from my_project.auth.service import accounts_devices_service
    accounts_devices_service.detach(account_id, device_id)
    return "", 204


def get_library(account_id):
    from my_project.auth.dao import accounts_dao
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    return jsonify([e.to_dict() for e in account.library_entries]), 200


def get_company(account_id):
    from my_project.auth.dao import accounts_dao
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    if account.company is None:
        return jsonify([]), 200
    return jsonify([account.company.to_dict()]), 200
