from flask import Blueprint

mainbp = Blueprint('main', __name__)

from app.main import routes