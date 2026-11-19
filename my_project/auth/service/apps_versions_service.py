from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import apps_versions_dao, apps_dao


def get_all():
    return [v.to_dict() for v in apps_versions_dao.find_all()]


def get_by_id(version_id):
    version = apps_versions_dao.find_by_id(version_id)
    if version is None:
        abort(404)
    return version.to_dict()


def create(data):
    if apps_dao.find_by_id(data["app_id"]) is None:
        abort(400, description="app_id must reference an existing app")
    try:
        version = apps_versions_dao.create(data)
    except IntegrityError:
        abort(409, description="App version already exists")
    return version.to_dict()


def update(version_id, data, partial=False):
    version = apps_versions_dao.find_by_id(version_id)
    if version is None:
        abort(404)
    if "app_id" in data and apps_dao.find_by_id(data["app_id"]) is None:
        abort(400, description="app_id must reference an existing app")
    try:
        version = apps_versions_dao.update(version, data)
    except IntegrityError:
        abort(409, description="App version already exists")
    return version.to_dict()


def delete(version_id):
    version = apps_versions_dao.find_by_id(version_id)
    if version is None:
        abort(404)
    if version.installations:
        abort(409, description="Cannot delete version that has installations")
    try:
        apps_versions_dao.delete(version)
    except IntegrityError:
        abort(409, description="Cannot delete version due to related records")


def get_installations(version_id):
    version = apps_versions_dao.find_by_id(version_id)
    if version is None:
        abort(404)
    return [i.to_dict() for i in version.installations]
