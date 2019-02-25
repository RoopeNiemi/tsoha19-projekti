from application import db
from application.models import Base
from application.discussions.models import discussion_tag

class Tag(Base):

    name = db.Column(db.String(200), nullable=False)

    def __init__(self, name):
        self.name = name
