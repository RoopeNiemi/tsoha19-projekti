from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField

class DiscussionForm(FlaskForm):
    title = StringField("Title")
    content = TextAreaField("Content")

    def validate_form(self):
        if len(self.title.data.split()) > 30 or len(self.content.data.split()) > 300:
            return False

        return True

class CommentForm(FlaskForm):
    comment = TextAreaField("Comment")
    
    def validate_form(self):
        if len(self.comment.data.split()) <= 300 and len(self.comment.data)< 0:
            return True

        return False