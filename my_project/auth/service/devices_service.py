from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import devices_dao


def get_all():
    return [d.to_dict() for d in devices_dao.find_all()]


def get_by_id(device_id):
    device = devices_dao.find_by_id(device_id)
    if device is None:
        abort(404)
    return device.to_dict()


def create(data):
    try:
        device = devices_dao.create(data)
    except IntegrityError:
        abort(409, description="Device model+os_version already exists")
    return device.to_dict()


def update(device_id, data, partial=False):
    device = devices_dao.find_by_id(device_id)
    if device is None:
        abort(404)
    try:
        device = devices_dao.update(device, data)
    except IntegrityError:
        abort(409, description="Device model+os_version already exists")
    return device.to_dict()


def delete(device_id):
    device = devices_dao.find_by_id(device_id)
    if device is None:
        abort(404)
    try:
        devices_dao.delete(device)
    except IntegrityError:
        abort(409, description="Cannot delete device due to related records")


def get_installations(device_id):
    device = devices_dao.find_by_id(device_id)
    if device is None:
        abort(404)
    return [i.to_dict() for i in device.installations]
