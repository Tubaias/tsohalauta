from application import db

class User(db.Model):
    __tablename__ = "moderator"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    actions_taken = db.Column(db.Integer, default=0)

    messages = db.relationship("Message", backref='moderator', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
class Authkey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    akey = db.Column(db.String(144), nullable=False)

    def __init__(self, akey):
        self.akey = key