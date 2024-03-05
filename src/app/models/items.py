from app import db


class Item(db.Model):
    __tablename__ = "Data"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Item {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "date_added": self.date_added,
        }
