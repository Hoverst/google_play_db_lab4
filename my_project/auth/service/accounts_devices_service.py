from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import accounts_dao, devices_dao, accounts_devices_dao


def list_devices(account_id):
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    return [d.to_dict() for d in account.devices]


def list_accounts(device_id):
    device = devices_dao.find_by_id(device_id)
    if device is None:
        abort(404)
    return [a.to_dict() for a in device.accounts if a.deleted_at is None]


def attach(account_id, device_id):
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    device = devices_dao.find_by_id(device_id)
    if device is None:
        abort(404)
    if accounts_devices_dao.find_link(account_id, device_id) is not None:
        abort(409, description="Account already linked to this device")
    try:
        link = accounts_devices_dao.create_link(account_id, device_id)
    except IntegrityError:
        abort(409, description="Account already linked to this device")
    return link.to_dict()


def detach(account_id, device_id):
    account = accounts_dao.find_by_id_active(account_id)
    if account is None:
        abort(404)
    link = accounts_devices_dao.find_link(account_id, device_id)
    if link is None:
        abort(404)
    accounts_devices_dao.delete_link(link)
