from . import db
from datetime import datetime

class AuthLog(db.Model):
    __tablename__ = 'auth_logs'

    id = db.Column(db.Integer, primary_key=True)
    request_ip = db.Column(db.Text, nullable=False)
    request_timestamp = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref=db.backref('auth_logs', lazy=True))

    def __repr__(self):
        return f'<AuthLog {self.id} - User ID: {self.user_id}>'
