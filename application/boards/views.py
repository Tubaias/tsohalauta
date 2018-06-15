from flask import redirect, render_template, request, url_for

from application import app, db
from application.threads.models import Thread
from application.boards.models import Board

@app.route("/<board>/")
def boards_index(board):
    return render_template("boards/board_main.html", board = Board.query.get(board), threads = Thread.query.filter_by(board_id=board).order_by(Thread.activity))