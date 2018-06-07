from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm
from application.threads.models import Thread

@app.route("/t/<thread>/", methods=["GET"])
def messages_index(thread):
    return render_template("messages/list.html", messages = Message.query.filter_by(thread_id=thread), thread = Thread.query.get(thread), form = MessageForm())

@app.route("/t/<thread>/", methods=["POST"])
def messages_create(thread):
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messages/list.html", messages = Message.query.filter_by(thread_id=thread), thread = Thread.query.get(thread), form = form)

    m = Message(form.text.data, thread)
    
    if current_user.is_authenticated:
        m.moderator_id = current_user.id
        m.name = current_user.username
        current_user.actions_taken += 1

    threads = Thread.query.all()

    for t in threads:
        t.activity -= 1

    current_thread = Thread.query.get(thread)
    current_thread.activity += Thread.query.count() + 1
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("messages_index", thread=thread))

@app.route("/m/<message>/", methods=["GET"])
def messages_single(message):
    thread_id = Message.query.get(message).thread_id

    return render_template("messages/info.html", message = Message.query.get(message), thread = thread_id, form = MessageForm())

@app.route("/m/<message>/", methods=["POST"])
@login_required
def messages_edit(message):
    message_num = int(message[9:(len(message) - 1)])
    thread_id = Message.query.get(message_num).thread_id
    m = Message.query.get(message_num)

    if m is None:
        return redirect(url_for("messages_index", thread=thread_id))
        
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messages/info.html", message = Message.query.get(message_num), thread = thread_id, form = form)

    m.text = form.text.data
    current_user.actions_taken += 1
    db.session.commit()

    return redirect(url_for("messages_index", thread=thread_id))

@app.route("/m/<message>/delete", methods=["POST"])
@login_required
def messages_delete(message):
    message_num = int(message[9:(len(message) - 1)])
    thread_id = Message.query.get(message_num).thread_id
    m = Message.query.get(message_num)

    if m is None:
        return redirect(url_for("messages_index", thread=thread_id))

    threads = Thread.query.all()

    for t in threads:
        t.activity += 1

    current_thread = Thread.query.get(thread_id)

    current_thread.activity -= Thread.query.count() + 1
    db.session.delete(m)
    current_user.actions_taken += 1
    db.session.commit()

    return redirect(url_for("messages_index", thread=thread_id))