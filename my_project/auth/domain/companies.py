from my_project import db

class Company(db.Model):

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(60), nullable=False, unique=True)
    contact_email = db.Column(db.String(255), nullable=True)
    developer_account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False, unique=True)

    account = db.relationship('Account', back_populates='companies', lazy='select')
    apps = db.relationship('App', back_populates='company', lazy='select')

    def to_dict(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'contact_email': self.contact_email,
            'developer_account_id': self.developer_account_id
        }
