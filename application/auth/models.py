from sqlalchemy.ext.hybrid import hybrid_property
import bcrypt
from application import db
from application.models import Base

class User(Base):
    __tablename__ = "account"

    username=db.Column(db.String(144), nullable=False, unique=True)
    _password=db.Column(db.String(144), nullable=False)

    discussions = db.relationship("Discussion", cascade='all', backref='account', lazy=True)
    messages = db.relationship("Message", cascade='all', backref='account', lazy=True)
    role=db.Column(db.String(20), default="User",  nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self._password = password
    def get_id(self):
        return self.id
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @hybrid_property
    def password(self):
        return self._password

    
    def is_correct_password(self, plaintext):
        return bcrypt.checkpw(plaintext.encode('utf8'), self._password.encode('utf8'))
