from flask_sqlalchemy import SQLAlchemy
from constants import LeadStatus

db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    company = db.Column(db.String(100))
    notes = db.Column(db.Text)
    status = db.Column(db.String(50), default=LeadStatus.NEW_LEAD, nullable=False)  # Default status
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
