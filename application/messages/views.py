from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.messages.models import Message
from application.messages.forms import MessageForm

@app.route("/t/<thread>/", methods=["GET"])
def messages_index(thread):
    return render_template("messages/list.html", messages = Message.query.filter_by(thread_id=thread), thread = thread, form = MessageForm())

@app.route("/t/<thread>/", methods=["POST"])
def messages_create(thread):
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messages/list.html", messages = Message.query.filter_by(thread_id=thread), thread = thread, form = form)

    m = Message(form.text.data, thread)
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("messages_index", thread=thread))

@app.route("/m/<message>/", methods=["GET"])
def messages_single(message):
    thread_id = Message.query.get(message).thread_id

    return render_template("messages/edit.html", message = Message.query.get(message), thread = thread_id, form = MessageForm())

@app.route("/m/<message>/", methods=["POST"])
@login_required
def messages_edit(message):
    message_num = int(message[9:(len(message) - 1)])
    thread_id = Message.query.get(message_num).thread_id
    m = Message.query.get(message_num)

    if m is None:
        return redirect(url_for("messages_index", thread=thread_id))
    else:
        form = MessageForm(request.form)

        if not form.validate():
            return render_template("messages/edit.html", message = Message.query.get(message_num), thread = thread_id, form = form)

        m.text = form.text.data
        db.session.commit()
        return redirect(url_for("messages_index", thread=thread_id))