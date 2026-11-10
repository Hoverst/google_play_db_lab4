from my_project import db
from my_project.auth.domain.installations import Installation

def find_all():
    return Installation.query.all()

def find_by_id(app_id, device_id):
    return Installation.query.get((app_id, device_id))

def create(data):
    instance = Installation(**data)
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
