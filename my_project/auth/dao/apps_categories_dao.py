from my_project import db
from my_project.auth.domain.apps_categories import AppCategory


def find_link(app_id, category_id):
    return db.session.get(AppCategory, (app_id, category_id))


def create_link(app_id, category_id):
    instance = AppCategory(app_id=app_id, category_id=category_id)
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
