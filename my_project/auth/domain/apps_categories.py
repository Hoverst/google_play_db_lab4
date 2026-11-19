from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class AppCategory(db.Model):
    __tablename__ = "apps_categories"

    app_id = db.Column(
        INTEGER(unsigned=True), db.ForeignKey("apps.id", ondelete="CASCADE"), primary_key=True
    )
    category_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("categories.id", ondelete="RESTRICT"),
        primary_key=True,
    )

    app = db.relationship("App", lazy="select", overlaps="apps,categories")
    category = db.relationship("Category", lazy="select", overlaps="apps,categories")

    def to_dict(self):
        return {"app_id": self.app_id, "category_id": self.category_id}
