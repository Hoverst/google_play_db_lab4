from my_project import db
from my_project.auth.domain.apps import App
from my_project.auth.domain.apps_versions import AppVersion
from my_project.auth.domain.library import Library
from my_project.auth.domain.reviews import Review


def find_all():
    return App.query.all()


def has_dependents(app_id):
    """True if the app still has versions, library entries, or reviews."""
    return (
        db.session.query(AppVersion.id).filter_by(app_id=app_id).first() is not None
        or db.session.query(Library.id).filter_by(app_id=app_id).first() is not None
        or db.session.query(Review.id).filter_by(app_id=app_id).first() is not None
    )


def find_by_id(id):
    return db.session.get(App, id)


def create(data):
    instance = App(**data)
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
