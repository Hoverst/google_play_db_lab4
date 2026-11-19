from datetime import datetime, timezone
from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import accounts_dao
from my_project.utils.password import hash_password


def get_all():
    return [a.to_dict() for a in accounts_dao.find_all_active()]


def get_by_id(account_id):
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    return account.to_dict()


def create(data):
    payload = {
        "email": data["email"],
        "password_hash": hash_password(data["password"]),
        "name": data["name"],
    }
    try:
        account = accounts_dao.create(payload)
    except IntegrityError:
        abort(409, description="Email already exists")
    return account.to_dict()


def update(account_id, data, partial=False):
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    payload = {}
    if "email" in data:
        payload["email"] = data["email"]
    if "name" in data:
        payload["name"] = data["name"]
    if "password" in data:
        payload["password_hash"] = hash_password(data["password"])
    try:
        account = accounts_dao.update(account, payload)
    except IntegrityError:
        abort(409, description="Email already exists")
    return account.to_dict()


def delete(account_id):
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    accounts_dao.soft_delete(account, datetime.now(timezone.utc).replace(tzinfo=None))


def get_library(account_id):
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    return [e.to_dict() for e in account.library_entries]


def get_company(account_id):
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    if account.company is None:
        return []
    return [account.company.to_dict()]
