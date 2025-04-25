from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)  # Дата регистрации
    balance = db.Column(db.Float, default=1000)  # Стартовый баланс

    def __repr__(self):
        return f"<User {self.username}>"
