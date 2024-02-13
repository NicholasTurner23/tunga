from flask import Blueprint

postbp = Blueprint('posts', __name__)

from app.posts import routes