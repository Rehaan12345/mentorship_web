from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager 
# If doesn't work - pip install werkzeug==2.3.0
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail, Message
import os


db = SQLAlchemy()
DB_NAME = "database.db"

admin = Admin()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "rehaan"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}" 
    db.init_app(app) 

    from .views import views
    from .auth import auth

    from .models import User 

    with app.app_context():
        db.create_all()
        admin.init_app(app)

    admin.add_view(ModelView(User, db.session))

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app) 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    app.register_blueprint(views, url_prefix="/")

    return app