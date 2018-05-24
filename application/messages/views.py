from application import app, db
from flask import redirect, render_template, request, url_for
from application.messages.models import Message

@app.route("/t/<thread>/", methods=["GET"])
def messages_index(thread):
    return render_template("messages/list.html", messages = Message.query.filter_by(thread_id=thread), thread = thread)

@app.route("/t/<thread>/", methods=["POST"])
def messages_create(thread):
    m = Message(request.form.get("text"), thread)
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("messages_index", thread=thread))

@app.route("/m/<message>/", methods=["GET"])
def messages_single(message):
    thread_id = Message.query.get(message).thread_id

    return render_template("messages/edit.html", message = Message.query.get(message), thread = thread_id)

@app.route("/m/<message>/", methods=["POST"])
def messages_edit(message):
    message_num = int(message[9:(len(message) - 1)])
    thread_id = Message.query.get(message_num).thread_id
    m = Message.query.get(message_num)

    if m is None:
        return redirect(url_for("messages_index", thread=thread_id))
    else:
        m.text = request.form.get("text")
        db.session.commit()
        return redirect(url_for("messages_index", thread=thread_id))