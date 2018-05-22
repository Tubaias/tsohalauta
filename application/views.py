from flask import render_template
from application import app
from application.messages.models import Message

@app.route("/")
def index():
    messagelist = Message.query.distinct(Message.thread_id)
    messageset = set()
    for m in messagelist:
        messageset.add(m.thread_id)

    return render_template("index.html", threads = messageset)