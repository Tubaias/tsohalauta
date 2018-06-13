from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, validators

class MessageForm(FlaskForm):
    text = StringField("Message text", [validators.Length(min=1), validators.Length(max=1000)])
    target = HiddenField()

    def set_reply(self, reply):
        self.target.data = reply

    class Meta:
        csrf = False
