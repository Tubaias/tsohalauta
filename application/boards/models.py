from sqlalchemy.sql import text

from application import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(3), nullable=False)

    threads = db.relationship("Thread", cascade="delete", lazy=True)

    def __init__(self, tag):
        self.tag = tag

    @staticmethod
    def get_all_boards_total_activity():
        stmt = text("SELECT Board.id, Board.tag, SUM(Thread.activity) AS activity FROM Board"
                    " LEFT JOIN Thread ON Thread.board_id = Board.id"
                    " GROUP BY Board.id"
                    " ORDER BY activity DESC")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "tag":row[1], "activity":row[2]})

        return response