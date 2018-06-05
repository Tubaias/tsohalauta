from flask import render_template
from application import app
from application.messages.models import Message
from application.threads.models import Thread

@app.route("/")
def index():
    return render_template("index.html", threads = Thread.query.all())