from application import db
from application.discussions.models import discussion_tag

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
    onupdate=db.func.current_timestamp(), nullable=False)

    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name
