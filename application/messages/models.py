from application import db
from application.models import Base
class Message(Base):
    content = db.Column(db.String(2000), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    discussion_id = db.Column(db.Integer, db.ForeignKey('discussion.id'), nullable=False)

    def __init__(self, content):
        self.content = content

    def set_discussion_id(self,  id):
        self.discussion_id = id

    def set_account_id(self, id):
        self.account_id = id