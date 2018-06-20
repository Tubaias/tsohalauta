from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.threads.forms import ThreadForm

@app.route("/<board>/new", methods = ["GET", "POST"])
def threads_create(board):
    if request.method == "GET":
        return render_template("threads/threadform.html", form = ThreadForm(), board = board)

    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/threadform.html", form = form, board = board)

    t = Thread(form.title.data, form.text.data, board)

    if current_user.is_authenticated:
        t.moderator_id = current_user.id
        t.name = current_user.username
        current_user.actions_taken += 1

    if Thread.query.count() >= 20:
        least_active_thread = Thread.query.order_by(Thread.activity).first()
        db.session.delete(least_active_thread)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("messages_index", thread=t.id))

@app.route("/t/<thread>/info", methods = ["GET"])
def threads_info(thread):
    return render_template("threads/info.html", thread = Thread.query.get(thread), form = ThreadForm())

@app.route("/t/<thread>/info", methods=["POST"])
@login_required
def threads_edit(thread):
    t = Thread.query.get(thread)

    if t is None:
        return redirect(url_for("index"))

    board_id = t.board_id
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/info.html", thread = t, form = form)

    t.title = form.title.data
    t.text = form.text.data
    current_user.actions_taken += 1
    db.session.commit()

    return redirect(url_for("boards_index", board=board_id))

@app.route("/t/<thread>/del", methods = ["GET", "POST"])
@login_required
def threads_delete(thread):
    t = Thread.query.get(thread)
    board = t.board_id
    db.session.delete(t)
    current_user.actions_taken += 1

    db.session().commit()
    return redirect(url_for("boards_index", board=board))