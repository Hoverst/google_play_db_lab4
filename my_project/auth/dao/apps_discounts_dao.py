from my_project import db
from my_project.auth.domain.apps_discounts import AppDiscount

def find_all():
    return AppDiscount.query.all()

def find_by_id(id):
    return AppDiscount.query.get(id)

def create(data):
    instance = AppDiscount(**data)
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
