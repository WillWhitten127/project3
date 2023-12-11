from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True)
    date_registered = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    last_login = db.Column(db.TIMESTAMP)

    def __repr__(self):
        return f'<User {self.username}>'
