from flask import Blueprint

userbp = Blueprint('users', __name__, template_folder="templates")

from app.users import routes