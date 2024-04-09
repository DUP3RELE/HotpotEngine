from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.String(32), unique=True, nullable=False)
    restaurantname = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    employees = db.relationship('Employee', backref='restaurant', lazy='dynamic')
