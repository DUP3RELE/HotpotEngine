from . import db


class Position(db.Model):
    __tablename__ = 'position'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    access = db.Column(db.String(100), nullable=True)
