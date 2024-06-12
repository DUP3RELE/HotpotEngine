from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    restaurantname = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # Assuming `restaurant_id` is not needed
    # restaurant_id = db.Column(db.String(32), unique=True, nullable=False)

    employees = db.relationship('Employee', backref='restaurant', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Restaurant {self.restaurantname}>'
