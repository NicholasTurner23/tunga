from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
loginmanager = LoginManager()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    loginmanager.init_app(app)
    Bootstrap5(app)

    #Blue prints
    from app.main import mainbp as main_bp
    app.register_blueprint(main_bp)
    
    from app.posts import postbp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.users import userbp as user_bp
    app.register_blueprint(user_bp, url_prefix='/auth')

    return app

def get_db():
    return db

def get_loginmanager():
    return loginmanager