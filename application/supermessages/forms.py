from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class SuperMessageForm(FlaskForm):
    text = TextAreaField("Supermessage text", [validators.Length(min=1), validators.Length(max=250)])

    class Meta:
        csrf = False
