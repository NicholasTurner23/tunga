from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

class PostFrom(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(32)])
    description = TextAreaField("Description", validators=[DataRequired(), Length(255)])
    author = StringField("Author", validators=[DataRequired(), Length(32)])
    submit = SubmitField("Submit")