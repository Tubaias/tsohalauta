from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MessageForm(FlaskForm):
    text = StringField("Message text", [validators.Length(min=1), validators.Length(max=1000)])
 
    class Meta:
        csrf = False
