from datetime import datetime, timezone
from . import db


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    guest_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    guests_number = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    date_reserved = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
