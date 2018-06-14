from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.threads.models import Thread
from application.threads.forms import ThreadForm

@app.route("/thread/new", methods = ["GET", "POST"])
def threads_create():
    if request.method == "GET":
        return render_template("threads/threadform.html", form = ThreadForm())

    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/threadform.html", form = form)

    t = Thread(form.title.data, form.text.data, 1)

    if current_user.is_authenticated:
        t.moderator_id = current_user.id
        t.name = current_user.username

    if Thread.query.count() >= 20:
        least_active_thread = Thread.query.order_by(Thread.activity).first()
        db.session.delete(least_active_thread)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("messages_index", thread=t.id))

@app.route("/t/<thread>/del", methods = ["GET", "POST"])
@login_required
def threads_delete(thread):
    t = Thread.query.get(thread)
    db.session.delete(t)
    current_user.actions_taken += 1

    db.session().commit()
    return redirect(url_for("index"))