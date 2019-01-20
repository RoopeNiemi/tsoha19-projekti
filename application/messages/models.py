from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
    onupdate=db.func.current_timestamp())

    content = db.Column(db.String(300), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    discussion_id = db.Column(db.Integer, db.ForeignKey('discussion.id'), nullable=False)

    def __init__(self, content):
        self.content = content

    def set_discussion_id(self,  id):
        self.discussion_id = id

    def set_account_id(self, id):
        self.account_id = id