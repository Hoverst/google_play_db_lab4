from my_project import db

class AppDiscount(db.Model):

    __tablename__ = 'apps_discounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    discount_price = db.Column(db.Numeric(10, 2), nullable=False)
    starts_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    ends_at = db.Column(db.DateTime, nullable=False)

    app = db.relationship('App', back_populates='discounts', lazy='select')
    bills = db.relationship(
        'Bill',
        back_populates='discount',
        lazy='select',
        primaryjoin='AppDiscount.id == Bill.discount_id',
        foreign_keys='Bill.discount_id'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'app_id': self.app_id,
            'discount_price': float(self.discount_price) if self.discount_price is not None else None,
            'starts_at': self.starts_at.isoformat() if self.starts_at else None,
            'ends_at': self.ends_at.isoformat() if self.ends_at else None
        }
