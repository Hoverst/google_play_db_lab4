from my_project import db
from my_project.auth.domain.apps_categories import AppCategory

def find_all():
    return AppCategory.query.all()

def find_by_id(app_id, category_id):
    return AppCategory.query.get((app_id, category_id))

def create(data):
    instance = AppCategory(**data)
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
