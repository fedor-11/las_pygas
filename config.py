import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///casino.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
