from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(60), nullable=False, unique=True)
    contact_email = db.Column(db.String(255), nullable=True)
    developer_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("accounts.id", ondelete="RESTRICT"),
        nullable=False,
        unique=True,
    )

    developer = db.relationship("Account", back_populates="company", lazy="select")
    apps = db.relationship("App", back_populates="company", lazy="select")

    def to_dict(self):
        return {
            "id": self.id,
            "company_name": self.company_name,
            "contact_email": self.contact_email,
            "developer_id": self.developer_id,
        }
