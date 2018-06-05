from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
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

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("messages_index", thread=t.id))