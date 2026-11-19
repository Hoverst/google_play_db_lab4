import enum
from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class AppStatus(str, enum.Enum):
    published = "published"
    unpublished = "unpublished"
    suspended = "suspended"


class App(db.Model):
    __tablename__ = "apps"

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    package_name = db.Column(db.String(150), nullable=False, unique=True)
    caption = db.Column(db.String(600), nullable=True)
    company_id = db.Column(
        INTEGER(unsigned=True), db.ForeignKey("companies.id", ondelete="RESTRICT"), nullable=False
    )
    status = db.Column(
        db.Enum(AppStatus, values_callable=lambda x: [e.value for e in x], native_enum=True),
        nullable=False,
        server_default="published",
    )

    company = db.relationship("Company", back_populates="apps", lazy="select")
    categories = db.relationship(
        "Category", secondary="apps_categories", back_populates="apps", lazy="select"
    )
    versions = db.relationship("AppVersion", back_populates="app", lazy="select")
    library_entries = db.relationship("Library", back_populates="app", lazy="select")
    reviews = db.relationship(
        "Review",
        primaryjoin="App.id==foreign(Review.app_id)",
        viewonly=True,
        lazy="select",
    )

    def to_dict(self):
        status = self.status.value if isinstance(self.status, AppStatus) else self.status
        return {
            "id": self.id,
            "title": self.title,
            "package_name": self.package_name,
            "caption": self.caption,
            "company_id": self.company_id,
            "status": status,
        }
