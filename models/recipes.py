from datetime import datetime, timezone
from . import db


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content_ingredients = db.Column(db.Text, nullable=False)
    content_methods = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)
    editor_name = db.Column(db.String(64), nullable=False)
