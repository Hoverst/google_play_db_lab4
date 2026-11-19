from datetime import datetime, timezone
from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import installations_dao, devices_dao, apps_versions_dao


def get_all():
    return [i.to_dict() for i in installations_dao.find_all()]


def get_by_id(installation_id):
    inst = installations_dao.find_by_id(installation_id)
    if inst is None:
        abort(404)
    return inst.to_dict()


def create(data):
    if devices_dao.find_by_id(data["device_id"]) is None:
        abort(400, description="device_id must reference an existing device")
    if apps_versions_dao.find_by_id(data["app_version_id"]) is None:
        abort(400, description="app_version_id must reference an existing app version")
    try:
        inst = installations_dao.create(data)
    except IntegrityError:
        abort(409, description="Installation already exists for this device and app version")
    return inst.to_dict()


def update(installation_id, data, partial=False):
    inst = installations_dao.find_by_id(installation_id)
    if inst is None:
        abort(404)
    if "device_id" in data and devices_dao.find_by_id(data["device_id"]) is None:
        abort(400, description="device_id must reference an existing device")
    if "app_version_id" in data and apps_versions_dao.find_by_id(data["app_version_id"]) is None:
        abort(400, description="app_version_id must reference an existing app version")
    payload = dict(data)
    payload["updated_at"] = datetime.now(timezone.utc).replace(tzinfo=None)
    try:
        inst = installations_dao.update(inst, payload)
    except IntegrityError:
        abort(409, description="Installation already exists for this device and app version")
    return inst.to_dict()


def delete(installation_id):
    inst = installations_dao.find_by_id(installation_id)
    if inst is None:
        abort(404)
    installations_dao.delete(inst)
