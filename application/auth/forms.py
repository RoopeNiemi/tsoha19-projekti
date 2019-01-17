from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class UsernameAndPasswordForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")