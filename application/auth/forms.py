from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class UsernameAndPasswordForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    def validate_form(self):
        if len(self.username.data) < 6 or len(self.password.data) < 8:
            return False

        return True