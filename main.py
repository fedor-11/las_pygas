from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from models.user import db, User
from routes.auth import auth_bp
from routes.profile import profile_bp

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    # Регистрируем blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)