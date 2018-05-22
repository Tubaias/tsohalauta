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