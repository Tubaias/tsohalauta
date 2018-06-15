from application import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(3), nullable=False)

    threads = db.relationship("Thread", cascade="delete", lazy=True)

    def __init__(self, tag):
        self.tag = tag