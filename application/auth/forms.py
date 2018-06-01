from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3), validators.Length(max=144)])
    password = PasswordField("Password", [validators.Length(min=3), validators.Length(max=144)])
    authkey = PasswordField("Authorization key")
  
    class Meta:
        csrf = False
