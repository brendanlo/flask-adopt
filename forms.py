from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, Length, URL

"""Forms for adopt app."""


class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species',
                          validators=[
                              InputRequired(),
                              AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = SelectField('Age', choices=[
        ('baby', 'Baby'),
        ('young', 'Young'),
        ('adult', 'Adult'),
        ('senior', 'Senior')],
        validators=[
            InputRequired(),
            AnyOf(['baby', 'young', 'adult', 'senior'])])
    notes = TextAreaField('Notes', validators=[Optional(), Length(max=1000)])


class EditPetForm(FlaskForm):
    """Form to edit pet information"""

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional(), Length(max=1000)])
    available = BooleanField(
        'Available for Adoption')
