from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField

"""Forms for adopt app."""


class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField('Pet Name')
    species = StringField('Species')
    photo_url = StringField('Photo URL')
    age = SelectField('Age', choices=[
        ('baby', 'Baby'),
        ('young', 'Young'),
        ('adult', 'Adult'),
        ('senior', 'Senior')])
    notes = TextAreaField('Notes')
