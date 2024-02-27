from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class PostFrom(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(10, 32)])
    description = TextAreaField("Description", validators=[DataRequired(), Length(20, 255)])
    # author = SelectField('User', coerce=int, validators=[DataRequired()], choices=[(user.id, user.username) for user in User.query.all()])
    submit = SubmitField("Submit")