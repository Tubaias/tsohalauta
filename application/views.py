from flask import render_template

from application import app
from application.boards.models import Board

@app.route("/")
def index():
    return render_template("index.html", boards = Board.query.all())