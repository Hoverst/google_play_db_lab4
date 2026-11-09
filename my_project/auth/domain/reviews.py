# reviews.py - SQLAlchemy model for the 'reviews' table

from my_project import db


class Review(db.Model):
    """Represents a user review for an app in the play_store database."""

    __tablename__ = 'reviews'
    __table_args__ = (
        db.PrimaryKeyConstraint('account_id', 'app_id'),
    )

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    rating = db.Column(db.Numeric(2, 1), nullable=False)
    comment = db.Column(db.String(350), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    # Relationships
    account = db.relationship('Account', back_populates='reviews', lazy='select')
    app = db.relationship('App', back_populates='reviews', lazy='select')

    def to_dict(self):
        """Convert all columns to a JSON-safe dictionary."""
        return {
            'account_id': self.account_id,
            'app_id': self.app_id,
            'rating': float(self.rating) if self.rating is not None else None,
            'comment': self.comment,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
