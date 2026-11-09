# accounts.py - SQLAlchemy model for the 'accounts' table

from my_project import db


class Account(db.Model):
    """Represents a user account in the play_store database."""

    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(70), nullable=False)
    is_developer = db.Column(db.SmallInteger, nullable=False, default=0)
    country = db.Column(db.String(70), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    # Relationships
    devices = db.relationship('Device', secondary='accounts_devices', back_populates='accounts', lazy='select')
    companies = db.relationship('Company', back_populates='account', lazy='select')
    payment_cards = db.relationship('PaymentCard', back_populates='account', lazy='select')
    reviews = db.relationship('Review', back_populates='account', lazy='select')
    bills = db.relationship('Bill', back_populates='account', lazy='select')
    library_entries = db.relationship('Library', back_populates='account', lazy='select')

    def to_dict(self):
        """Convert all columns to a JSON-safe dictionary."""
        return {
            'id': self.id,
            'email': self.email,
            'password_hash': self.password_hash,
            'name': self.name,
            'is_developer': self.is_developer,
            'country': self.country,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
