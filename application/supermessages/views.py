from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.supermessages.models import SuperMessage
from application.supermessages.forms import SuperMessageForm

@app.route("/<board>/super", methods = ["GET", "POST"])
@login_required
def supermessages_create(board):
    if request.method == "GET":
        return render_template("supermessages/supermessageform.html", form = SuperMessageForm(), board = board)

    form = SuperMessageForm(request.form)

    if not form.validate():
        return render_template("supermessages/supermessageform.html", form = form, board = board)

    sm = SuperMessage(current_user.username, form.text.data)
    sm.moderator_id = current_user.id
    current_user.actions_taken += 1

    threads = Thread.query.filter_by(board_id=board)
    for thread in threads:
        thread.supermessages.append(sm)

    db.session().commit()

    return redirect(url_for("boards_index", board=board))

@app.route("/s/<super>/delete", methods = ["GET", "POST"])
@login_required
def supermessages_delete(super):
    sm = SuperMessage.query.get(super)
    thread = request.args.get('thread')

    if sm is None:
        return redirect(url_for("index"))

    db.session.delete(sm)
    current_user.actions_taken += 1
    db.session.commit()

    return redirect(url_for("index"))