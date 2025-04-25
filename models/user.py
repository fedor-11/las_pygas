from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime


db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Integer, default=1000)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)  # Новое поле для даты и времени регистрации

    def __repr__(self):
        return f'<User {self.username}>'
