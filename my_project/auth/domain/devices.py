from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class Device(db.Model):
    __tablename__ = "devices"
    __table_args__ = (
        db.UniqueConstraint("model", "os_version", name="uq_devices_model_os_version"),
    )

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    model = db.Column(db.String(45), nullable=False)
    os_version = db.Column(db.String(20), nullable=False)

    accounts = db.relationship(
        "Account", secondary="accounts_devices", back_populates="devices", lazy="select"
    )
    installations = db.relationship(
        "Installation", back_populates="device", lazy="select", passive_deletes=True
    )

    def to_dict(self):
        return {"id": self.id, "model": self.model, "os_version": self.os_version}
