from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm
from application.threads.models import Thread

@app.route("/t/<thread>/", methods=["GET"])
def messages_index(thread):
    messages = Message.query.filter_by(thread_id=thread).order_by(Message.id)
    form = MessageForm()
    reply = request.args.get('reply')
    
    if reply != None:
        form.set_reply(reply)

    return render_template("messages/list.html", messages = messages, thread = Thread.query.get(thread), form = form)

@app.route("/t/<thread>/", methods=["POST"])
def messages_create(thread):
    thread_object = Thread.query.get(thread)

    form = MessageForm(request.form)
    if not form.validate():
        return render_template("messages/list.html", messages = Message.query.filter_by(thread_id=thread).order_by(Message.id), thread = thread_object, form = form)
    
    messagecount = len(thread_object.messages)
    if messagecount >= 100:
        return render_template("messages/list.html", messages = Message.query.filter_by(thread_id=thread).order_by(Message.id), thread = thread_object,
                                form = form, toomanymessages = "Cannot post message, this thread is over the message limit.")

    m = Message(form.text.data, thread)

    if form.target.data != None and form.target.data != "":
        m.reply_target_id = int(form.target.data)
    
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

@app.route("/m/<message>/info", methods=["GET"])
def messages_info(message):
    return render_template("messages/info.html", message = Message.query.get(message), form = MessageForm())

@app.route("/m/<message>/info", methods=["POST"])
@login_required
def messages_edit(message):
    m = Message.query.get(message)

    if m is None:
        return redirect(url_for("index"))

    thread_id = m.thread_id
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messages/info.html", message = m, thread = thread_id, form = form)

    m.text = form.text.data
    current_user.actions_taken += 1
    db.session.commit()

    return redirect(url_for("messages_index", thread=thread_id))

@app.route("/m/<message>/delete", methods=["POST"])
@login_required
def messages_delete(message):
    m = Message.query.get(message)

    if m is None:
        return redirect(url_for("index"))

    thread_id = m.thread_id
    threads = Thread.query.all()

    for t in threads:
        t.activity += 1

    current_thread = Thread.query.get(thread_id)

    current_thread.activity -= Thread.query.count() + 1
    db.session.delete(m)
    current_user.actions_taken += 1
    db.session.commit()

    return redirect(url_for("messages_index", thread=thread_id))