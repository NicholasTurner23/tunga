from flask import render_template
from app.main import mainbp


@mainbp.route('/')
def index():
    return render_template('index.html')
