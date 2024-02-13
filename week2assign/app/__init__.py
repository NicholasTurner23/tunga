from flask import Flask

def create_app():
    app = Flask(__name__)

    #Blue prints
    from app.main import mainbp as main_bp
    app.register_blueprint(main_bp)
    
    from app.posts import postbp as posts_bp
    app.register_blueprint(posts_bp)

    return app