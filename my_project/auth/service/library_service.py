from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import library_dao, accounts_dao, apps_dao, reviews_dao


def get_all():
    return [e.to_dict() for e in library_dao.find_all()]


def get_by_id(entry_id):
    entry = library_dao.find_by_id(entry_id)
    if entry is None:
        abort(404)
    return entry.to_dict()


def create(data):
    if accounts_dao.find_by_id_active(data["account_id"]) is None:
        abort(400, description="account_id must reference an existing non-deleted account")
    if apps_dao.find_by_id(data["app_id"]) is None:
        abort(400, description="app_id must reference an existing app")
    try:
        entry = library_dao.create(data)
    except IntegrityError:
        abort(409, description="Library entry already exists for this account and app")
    return entry.to_dict()


def update(entry_id, data, partial=False):
    entry = library_dao.find_by_id(entry_id)
    if entry is None:
        abort(404)
    if "account_id" in data and accounts_dao.find_by_id_active(data["account_id"]) is None:
        abort(400, description="account_id must reference an existing non-deleted account")
    if "app_id" in data and apps_dao.find_by_id(data["app_id"]) is None:
        abort(400, description="app_id must reference an existing app")
    changing_key = (
        ("account_id" in data and data["account_id"] != entry.account_id)
        or ("app_id" in data and data["app_id"] != entry.app_id)
    )
    if changing_key and reviews_dao.find_by_account_and_app(entry.account_id, entry.app_id) is not None:
        abort(409, description="Cannot change account_id or app_id while a review exists for this library entry")
    try:
        entry = library_dao.update(entry, data)
    except IntegrityError:
        abort(409, description="Library entry already exists for this account and app")
    return entry.to_dict()


def delete(entry_id):
    entry = library_dao.find_by_id(entry_id)
    if entry is None:
        abort(404)
    if reviews_dao.find_by_account_and_app(entry.account_id, entry.app_id) is not None:
        abort(409, description="Cannot delete library entry that has a review")
    try:
        library_dao.delete(entry)
    except IntegrityError:
        abort(409, description="Cannot delete library entry due to related records")
