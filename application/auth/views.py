from flask import render_template, request, redirect, url_for

from application import app
from application.auth.models import Moderator
from application.auth.forms import LoginForm


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    moderator = Moderator.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not moderator:
        return render_template("auth/loginform.html", form = form,
                               error = "Incorrect username or password")

    print("Moderator account " + moderator.name + " identified")
    return redirect(url_for("index"))