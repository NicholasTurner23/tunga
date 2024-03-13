from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
loginmanager = LoginManager()

ma = Marshmallow()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    loginmanager.init_app(app)
    ma.init_app(app)
    
    Bootstrap5(app)

    #Blue prints
    from app.errors import errors as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import mainbp as main_bp
    app.register_blueprint(main_bp)
    
    from app.posts import postbp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.users import userbp as user_bp
    app.register_blueprint(user_bp, url_prefix='/auth')

    from app.api import apibp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    from app.apiv2 import apibp2 as api_bp2
    app.register_blueprint(api_bp2, url_prefix='/api/v2')

    return app

def get_db():
    return db

def get_ma():
    return ma

def get_loginmanager():
    return loginmanager