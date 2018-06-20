from flask import redirect, render_template, request, url_for

from application import app, db
from application.messages.models import Message
from application.threads.models import Thread

@app.route("/search/", methods=["GET", "POST"])
def search_execute():
    searchtext = request.form.get("search")
    source = request.form.get("source")

    threads_title = []
    threads_text = []
    messages = []

    if source == "all":
        threads_title = Thread.query.filter(Thread.title.like("%" + searchtext + "%")).all()
        threads_text = Thread.query.filter(Thread.text.like("%" + searchtext + "%")).all()
        messages = Message.query.filter(Message.text.like("%" + searchtext + "%")).all()
    elif source == "threads":
        threads_title = Thread.query.filter(Thread.title.like("%" + searchtext + "%")).all()
        threads_text = Thread.query.filter(Thread.text.like("%" + searchtext + "%")).all()
    elif source == "messages":
        messages = Message.query.filter(Message.text.like("%" + searchtext + "%")).all()

    return render_template("search/results.html", threads_title = threads_title, threads_text = threads_text, messages = messages)