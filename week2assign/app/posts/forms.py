from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

class PostFrom(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    submit = SubmitField("Submit")