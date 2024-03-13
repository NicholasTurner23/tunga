from flask import Blueprint

apibp = Blueprint('api', __name__)

from app.api import routes
