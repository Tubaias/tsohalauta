from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User, Authkey
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Incorrect username or password")

    login_user(user)
    flash('Successfully logged in.')
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()

    if user:
        return render_template("auth/registerform.html", form = form, error = "Account already exists")

    key = Authkey.query.filter_by(keycode=form.authkey.data).first()

    if not key:
        return render_template("auth/registerform.html", form = form, error = "Incorrect authorization key")

    u = User(form.username.data, form.password.data)
    db.session().add(u)
    db.session().commit()

    flash('New account created.')
    return redirect(url_for("index"))