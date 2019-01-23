from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
# Could not get validators to work, these are just temporary.
class UsernameAndPasswordForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    def validate_form(self):
        if len(self.username.data) < 6 or len(self.password.data) < 8:
            return False

        return True

class CreateUserNamePasswordForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    repeat_password = PasswordField("Repeat password")

    def validate_form(self):
        if len(self.username.data) < 6 or len(self.password.data) < 8 or self.password.data != self.repeat_password.data:
            return False
        return True

class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField("Old password")
    new_password = PasswordField("New Password")
    repeat_new_password = PasswordField("Repeat new password")


    def validate_form(self):
        if len(self.new_password.data) < 8 or self.new_password.data != self.repeat_new_password.data or len(self.new_password.data) < 8:
            return False
        return True


class PasswordForm(FlaskForm):
    password = PasswordField("Password")