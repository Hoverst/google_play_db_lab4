from my_project import db
from my_project.auth.domain.apps_versions import AppVersion

def find_all():
    return AppVersion.query.all()

def find_by_id(id):
    return AppVersion.query.get(id)

def create(data):
    instance = AppVersion(**data)
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
