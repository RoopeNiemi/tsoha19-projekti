from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class UsernameAndPasswordForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])

class CreateUserNamePasswordForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=6,message='Username must be atleast 6 characters.')])
    password = PasswordField("Password", [validators.Length(min=8, message='Password must be atleast 8 characters.')])
    repeat_password = PasswordField("Repeat password", [validators.EqualTo('password', message='Passwords must match')])

    class Meta:
        csrf=False

class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField("Old password")
    new_password = PasswordField("New Password", [validators.Length(min=8), validators.EqualTo('repeat_new_password')])
    repeat_new_password = PasswordField("Repeat new password", [validators.Length(min=8)])


    class Meta:
        csrf=False


class PasswordForm(FlaskForm):
    password = PasswordField("Password")