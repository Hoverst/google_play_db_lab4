from my_project import db

class Bill(db.Model):

    __tablename__ = 'bills'
    __table_args__ = (
        db.PrimaryKeyConstraint('account_id', 'app_id'),
        db.ForeignKeyConstraint(
            ['payment_card_id', 'account_id'],
            ['payment_cards.id', 'payment_cards.account_id']
        ),
        db.ForeignKeyConstraint(
            ['discount_id', 'app_id'],
            ['apps_discounts.id', 'apps_discounts.app_id']
        ),
    )

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    currency = db.Column(db.String(3), nullable=False, default='USD')
    amount_paid = db.Column(db.Numeric(10, 2), nullable=False)
    payment_card_id = db.Column(db.Integer, nullable=False)
    paid_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    discount_id = db.Column(db.Integer, nullable=True)

    account = db.relationship('Account', back_populates='bills', lazy='select')
    app = db.relationship('App', back_populates='bills', lazy='select')
    payment_card = db.relationship(
        'PaymentCard',
        back_populates='bills',
        foreign_keys=[payment_card_id],
        lazy='select',
        primaryjoin='Bill.payment_card_id == PaymentCard.id'
    )
    discount = db.relationship(
        'AppDiscount',
        back_populates='bills',
        foreign_keys=[discount_id],
        lazy='select',
        primaryjoin='Bill.discount_id == AppDiscount.id'
    )

    def to_dict(self):
        return {
            'account_id': self.account_id,
            'app_id': self.app_id,
            'currency': self.currency,
            'amount_paid': float(self.amount_paid) if self.amount_paid is not None else None,
            'payment_card_id': self.payment_card_id,
            'paid_at': self.paid_at.isoformat() if self.paid_at else None,
            'discount_id': self.discount_id
        }
