from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField, validators

class DiscussionForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=5, max=100)])
    tags = StringField("Tags", [validators.Length(min=3, max=200)])
    content = TextAreaField("Content", [validators.Length(min=5, max=2000)])

    class Meta:
        csrf=False

class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", [validators.DataRequired(), validators.Length(max=2000)])
    
    class Meta:
        csrf=False