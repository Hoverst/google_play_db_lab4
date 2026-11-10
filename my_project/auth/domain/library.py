from my_project import db

class Library(db.Model):

    __tablename__ = 'library'
    __table_args__ = (
        db.PrimaryKeyConstraint('app_id', 'account_id'),
    )

    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    app_data = db.Column(db.JSON, nullable=True)
    last_opened_at = db.Column(db.DateTime, nullable=True)

    app = db.relationship('App', back_populates='library_entries', lazy='select')
    account = db.relationship('Account', back_populates='library_entries', lazy='select')

    def to_dict(self):
        return {
            'app_id': self.app_id,
            'account_id': self.account_id,
            'app_data': self.app_data,
            'last_opened_at': self.last_opened_at.isoformat() if self.last_opened_at else None
        }
