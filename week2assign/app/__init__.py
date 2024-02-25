from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    Bootstrap5(app)

    #Blue prints
    from app.main import mainbp as main_bp
    app.register_blueprint(main_bp)
    
    from app.posts import postbp as posts_bp
    app.register_blueprint(posts_bp)

    return app

def get_db():
    return db