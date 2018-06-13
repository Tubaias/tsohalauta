from application import db
from application.models import Base

class Message(Base):
    name = db.Column(db.String(144), default="Anonymous")
    text = db.Column(db.String(1000), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)
    moderator_id = db.Column(db.Integer, db.ForeignKey('moderator.id'), default=None)

    reply_target_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    replies = db.relationship("Message", lazy=True)

    def __init__(self, text, thread):
        self.text = text
        self.thread_id = thread