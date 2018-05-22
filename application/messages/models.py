from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate = db.func.current_timestamp())
    
    text = db.Column(db.String(1000), nullable=False)
    thread_id = db.Column(db.Integer, nullable=False)

    def __init__(self, text, thread):
        self.text = text
        self.thread_id = thread