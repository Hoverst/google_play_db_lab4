from my_project import db
from my_project.auth.domain.reviews import Review


def find_all():
    return Review.query.all()


def find_by_id(id):
    return db.session.get(Review, id)


def find_by_account_and_app(account_id, app_id):
    return Review.query.filter_by(account_id=account_id, app_id=app_id).first()


def create(data):
    instance = Review(**data)
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
