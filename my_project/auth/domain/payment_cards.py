from my_project import db

class PaymentCard(db.Model):

    __tablename__ = 'payment_cards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    token = db.Column(db.String(255), nullable=False, unique=True)
    card_brand = db.Column(db.String(30), nullable=False)
    exp_date = db.Column(db.Date, nullable=False)
    last4 = db.Column(db.String(4), nullable=False)

    account = db.relationship('Account', back_populates='payment_cards', lazy='select')
    bills = db.relationship(
        'Bill',
        back_populates='payment_card',
        lazy='select',
        primaryjoin='PaymentCard.id == Bill.payment_card_id',
        foreign_keys='Bill.payment_card_id'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'token': self.token,
            'card_brand': self.card_brand,
            'exp_date': self.exp_date.isoformat() if self.exp_date else None,
            'last4': self.last4
        }
