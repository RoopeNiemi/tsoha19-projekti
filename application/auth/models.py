from sqlalchemy.ext.hybrid import hybrid_property
import bcrypt
from application import db

class User(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
    onupdate=db.func.current_timestamp(), nullable=False)

    username=db.Column(db.String(144), nullable=False, unique=True)
    _password=db.Column(db.String(144), nullable=False)

    discussions = db.relationship("Discussion", backref='account', lazy=True)
    messages = db.relationship("Message", backref='account', lazy=True)
    
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

    @password.setter
    def set_password(self, plaintext):
        self._password = bcrypt.hashpw(plaintext, bcrypt.gensalt())

    
    def is_correct_password(self, plaintext):
        return bcrypt.checkpw(plaintext.encode('utf8'), self._password)