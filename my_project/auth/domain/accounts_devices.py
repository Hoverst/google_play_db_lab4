from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class AccountDevice(db.Model):
    __tablename__ = "accounts_devices"

    account_id = db.Column(
        INTEGER(unsigned=True), db.ForeignKey("accounts.id", ondelete="CASCADE"), primary_key=True
    )
    device_id = db.Column(
        INTEGER(unsigned=True), db.ForeignKey("devices.id", ondelete="CASCADE"), primary_key=True
    )

    account = db.relationship("Account", lazy="select", overlaps="accounts,devices")
    device = db.relationship("Device", lazy="select", overlaps="accounts,devices")

    def to_dict(self):
        return {"account_id": self.account_id, "device_id": self.device_id}
