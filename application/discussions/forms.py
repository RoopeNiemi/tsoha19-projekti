from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField, validators

class DiscussionForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired(), validators.Length(min=5, max=100)])
    content = TextAreaField("Content", [validators.Length(min=5, max=2000)])

    class Meta:
        csrf=False

class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", [validators.DataRequired(), validators.Length(max=2000)])
    
    class Meta:
        csrf=False