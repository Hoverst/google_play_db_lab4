from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(70), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    devices = db.relationship(
        "Device", secondary="accounts_devices", back_populates="accounts", lazy="select"
    )
    company = db.relationship("Company", back_populates="developer", uselist=False, lazy="select")
    library_entries = db.relationship("Library", back_populates="account", lazy="select")

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }
