from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, Label, Field
from wtforms.validators import DataRequired
import random

def get_stat():
    rolls = []
    total_value = 0
    for i in range(0, 4):
        dice_roll = random.randrange(1, 7)
        print(dice_roll)
        rolls.append(dice_roll)
    # remove smallest roll
    rolls.remove(min(rolls))

    # add up remaining three rolls
    for i in rolls:
        total_value += i
    return total_value

class CharacterForm(FlaskForm):
    character_name = StringField('Character Name', validators=[DataRequired()])
    attr1_val = get_stat()
    attr2_val = get_stat()
    attr3_val = get_stat()
    attr4_val = get_stat()
    attr5_val = get_stat()
    attr6_val = get_stat()

    attr1_label = Field('Attribute1: ')
    attr1_val = Field(str(attr1_val))
    attr2_label = Field('Attribute2: ')
    attr2_val = Field(str(attr2_val))
    attr3_label = Field('Attribute3: ')
    attr3_val = Field(str(attr3_val))
    attr4_label = Field('Attribute4: ')
    attr4_val = Field(str(attr4_val))
    attr5_label = Field('Attribute5: ')
    attr5_val = Field(str(attr5_val))
    attr6_label = Field('Attribute6: ')
    attr6_val = Field(str(attr6_val))

    reroll = SubmitField('Re-Roll Attributes',)
    submit = SubmitField('Save Character')