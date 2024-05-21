from datetime import datetime, timezone
from . import db


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    ingredients = db.relationship('Ingredient', backref='recipe', lazy=True)
    methods = db.relationship('Method', backref='recipe', lazy=True)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(20), nullable=False)


class Method(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)


