from my_project import db
from my_project.auth.domain.accounts import Account
from my_project.auth.domain.apps import AppStatus


def find_all_active():
    return Account.query.filter(Account.deleted_at.is_(None)).all()


def find_by_id_active(id):
    account = db.session.get(Account, id)
    if account is None or account.deleted_at is not None:
        return None
    return account


def find_by_id_any(id):
    return db.session.get(Account, id)


def find_by_email(email):
    return Account.query.filter_by(email=email).first()


def create(data):
    instance = Account(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def soft_delete(instance, deleted_at):
    try:
        instance.deleted_at = deleted_at
        company = instance.company
        if company is not None:
            for app in company.apps:
                if app.status != AppStatus.suspended:
                    app.status = AppStatus.unpublished
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise
