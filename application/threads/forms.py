from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ThreadForm(FlaskForm):
    title = StringField("Thread title", [validators.Length(min=1), validators.Length(max=32)])
    text = TextAreaField("Thread text", [validators.Length(min=1), validators.Length(max=1000)])
 
    class Meta:
        csrf = False