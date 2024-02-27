from flask import Blueprint

postbp = Blueprint('posts', __name__, template_folder="templates")

from app.posts import routes