from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    BooleanField,
    SelectField,
)
from wtforms.validators import InputRequired, URL, NumberRange


class AddPet(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        "Name", validators=[InputRequired(message="Name cannot be blank")]
    )
    species = SelectField(
        "Species",
        choices=[
            ("cat", "Cat"),
            ("dog", "Dog"),
            ("porcupine", "Porcupine"),
        ],
    )
    photo_url = StringField(
        "Photo URL", validators=[URL(message="Must be a valid URL")]
    )
    age = IntegerField(
        "Age",
        validators=[NumberRange(min=0, max=30, message="Age must be between 0 and 30")],
    )
    notes = StringField("Notes")
    available = BooleanField("Is available")


class EditPet(FlaskForm):
    """Form for editing pets"""

    photo_url = StringField(
        "Photo URL", validators=[URL(message="Must be a valid URL")]
    )
    notes = StringField("Notes")
    available = BooleanField("Is available")
