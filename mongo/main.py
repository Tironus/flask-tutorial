from flask import Blueprint, render_template, flash
from mongo import forms
from .db import create_doc
from .extensions import mongo_client

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = forms.CharacterForm()
    if form.validate_on_submit():
        mdb = mongo_client.OSRIC
        create_doc(mdb, form.character_name.data)
        flash('Character {} created...'.format(form.character_name.data))
    return render_template('character.html', form=form)