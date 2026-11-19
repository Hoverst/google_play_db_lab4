from my_project import db
from my_project.auth.domain.accounts_devices import AccountDevice


def find_link(account_id, device_id):
    return db.session.get(AccountDevice, (account_id, device_id))


def create_link(account_id, device_id):
    instance = AccountDevice(account_id=account_id, device_id=device_id)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete_link(instance):
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
