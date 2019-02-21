from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField, validators


class SearchTagForm(FlaskForm):
    tags = StringField("Tags", [validators.Length(min=3, max=200)])



    class Meta:
        csrf=False