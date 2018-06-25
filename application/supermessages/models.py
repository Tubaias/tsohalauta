from application import db
from application.models import Base

class SuperMessage(Base):
    __tablename__ = 'supermessage'
    
    name = db.Column(db.String(144), nullable=False)
    text = db.Column(db.String(1000), nullable=False)
    moderator_id = db.Column(db.Integer, db.ForeignKey('moderator.id'), default=None)

    def __init__(self, name, text):
        self.name = name
        self.text = text

ThreadSuperMessage = db.Table('ThreadSuperMessage',
    db.Column('thread_id', db.Integer, db.ForeignKey('thread.id')),
    db.Column('supermessage_id', db.Integer, db.ForeignKey('supermessage.id'))
)