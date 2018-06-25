from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, validators

class MessageForm(FlaskForm):
    text = TextAreaField("Message text", [validators.Length(min=1), validators.Length(max=500)])
    target = HiddenField()

    def set_reply(self, reply):
        self.target.data = reply

    class Meta:
        csrf = False
