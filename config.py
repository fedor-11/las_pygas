import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///casino.db'  # Путь к базе данных
    SQLALCHEMY_TRACK_MODIFICATIONS = False
