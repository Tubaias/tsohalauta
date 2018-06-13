from sqlalchemy.sql import text

from application import db
from application.models import Base

class Thread(Base):
    name = db.Column(db.String(144), default="Anonymous")
    title = db.Column(db.String(144))
    text = db.Column(db.String(1000), nullable=False)
    activity = db.Column(db.Integer, default=100)
    board_id = db.Column(db.Integer, nullable=False)
    moderator_id = db.Column(db.Integer, db.ForeignKey('moderator.id'), default=None)

    messages = db.relationship("Message", cascade="delete", lazy=True)

    def __init__(self, title, text, board):
        self.title = title
        self.text = text
        self.board_id = board

    @staticmethod
    def find_top10_threads():
        stmt = text("SELECT Thread.id, Thread.title, Thread.activity AS activity, COUNT(Message.id) AS messages FROM Thread"
                    " LEFT JOIN Message ON Message.thread_id = Thread.id"
                    " GROUP BY Thread.id"
                    " HAVING COUNT(Message.id) > 0"
                    " ORDER BY activity DESC, messages DESC"
                    " LIMIT 10")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "title":row[1], "activity":row[2], "messages":row[3]})

        return response
