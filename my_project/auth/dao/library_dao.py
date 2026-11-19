from my_project import db
from my_project.auth.domain.library import Library


def find_all():
    return Library.query.all()


def find_by_id(id):
    return db.session.get(Library, id)


def find_by_account_and_app(account_id, app_id):
    return Library.query.filter_by(account_id=account_id, app_id=app_id).first()


def create(data):
    instance = Library(**data)
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


def delete(instance):
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
