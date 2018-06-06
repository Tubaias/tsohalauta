from application import db
from application.models import Base

class Thread(Base):
    name = db.Column(db.String(144), default="Anonymous")
    title = db.Column(db.String(144))
    text = db.Column(db.String(1000), nullable=False)
    activity = db.Column(db.Integer, default=100)
    board_id = db.Column(db.Integer, nullable=False)
    moderator_id = db.Column(db.Integer, db.ForeignKey('moderator.id'), default=None)

    messages = db.relationship("Message", lazy=True)

    def __init__(self, title, text, board):
        self.title = title
        self.text = text
        self.board_id = board

    @staticmethod
    def find_threads_with_messages():
        stmt = text("SELECT Thread.id, Thread.title, Thread.activity FROM Thread"
                    " LEFT JOIN COUNT(Message) ON Message.thread_id = Thread.id"
                    " GROUP BY Thread.id"
                    " ORDER BY Thread.activity"
                    " HAVING COUNT(Message.id) > 0")

        res = db.engine.execute(stmt)
