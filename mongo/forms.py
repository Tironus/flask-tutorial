from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CharacterForm(FlaskForm):
    character_name = StringField('Character Name', validators=[DataRequired()])
    submit = SubmitField('Save Character')