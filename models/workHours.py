from datetime import datetime, timezone
from . import db


class WorkHours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.now(timezone.utc).date)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    end_time = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

