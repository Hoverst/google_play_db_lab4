from my_project import db
from my_project.auth.domain.library import Library

def find_all():
    return Library.query.all()

def find_by_id(app_id, account_id):
    return Library.query.get((app_id, account_id))

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
