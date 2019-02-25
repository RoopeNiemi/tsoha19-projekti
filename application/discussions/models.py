from application import db
from application.models import Base
from datetime import datetime
from sqlalchemy import Table, Integer, ForeignKey, Column

discussion_tag = Table('discussion_tag', db.Model.metadata,
    Column('discussion_id', Integer, ForeignKey('discussion.id')),
    Column('tag_id', Integer, ForeignKey('tag.id')))


class Discussion(Base):

    title = db.Column(db.String(100), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    messages = db.relationship("Message", backref='discussion', cascade='all',lazy=True)
    tags = db.relationship("Tag", cascade='all',secondary=discussion_tag, backref='discussions', lazy=True)

    def __init__(self, title):
        self.title = title

    def set_account_id(self, id):
        self.account_id = id

    def set_tags(self, tags):
        self.tags=tags


