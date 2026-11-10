from my_project import db
from my_project.auth.domain.payment_cards import PaymentCard

def find_all():
    return PaymentCard.query.all()

def find_by_id(id):
    return PaymentCard.query.get(id)

def create(data):
    instance = PaymentCard(**data)
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
