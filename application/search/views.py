from flask import redirect, render_template, request, url_for

from application import app, db
from application.messages.models import Message
from application.threads.models import Thread

@app.route("/search/", methods=["GET"])
def search_results():
    threads_title = request.args.get('threads_title')
    threads_text = request.args.get('threads_text')
    messages = request.args.get('messages')
    
    print("-------------------------------------------------------")
    print(threads_title)
    print(threads_text)
    print(messages)

    return render_template("search/results.html", threads_title = threads_title, threads_text = threads_text, messages = messages)

@app.route("/search/", methods=["POST"])
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

    print("-------------------------------------------------------")
    print(threads_title)
    print(threads_text)
    print(messages)

    #return redirect(url_for("search_results", threads_title = threads_title, threads_text = threads_text, messages = messages))
    return render_template("search/results.html", threads_title = threads_title, threads_text = threads_text, messages = messages)