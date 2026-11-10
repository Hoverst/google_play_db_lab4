from my_project import db
from my_project.auth.domain.devices import Device

def find_all():
    return Device.query.all()

def find_by_id(id):
    return Device.query.get(id)

def create(data):
    instance = Device(**data)
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
