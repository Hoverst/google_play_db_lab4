# apps.py - SQLAlchemy model for the 'apps' table

from my_project import db


class App(db.Model):
    """Represents an application in the play_store database."""

    __tablename__ = 'apps'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    caption = db.Column(db.String(600), nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    currency = db.Column(db.String(3), nullable=False, default='USD')
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)

    # Relationships
    company = db.relationship('Company', back_populates='apps', lazy='select')
    categories = db.relationship('Category', secondary='apps_categories', back_populates='apps', lazy='select')
    versions = db.relationship('AppVersion', back_populates='app', lazy='select')
    discounts = db.relationship('AppDiscount', back_populates='app', lazy='select')
    reviews = db.relationship('Review', back_populates='app', lazy='select')
    installations = db.relationship('Installation', back_populates='app', lazy='select')
    bills = db.relationship('Bill', back_populates='app', lazy='select')
    library_entries = db.relationship('Library', back_populates='app', lazy='select')

    def to_dict(self):
        """Convert all columns to a JSON-safe dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'caption': self.caption,
            'price': float(self.price) if self.price is not None else None,
            'currency': self.currency,
            'company_id': self.company_id
        }
