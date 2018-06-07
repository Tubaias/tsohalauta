from flask import redirect, render_template, request, url_for

from application import app, db
from application.threads.models import Thread

@app.route("/statistics/", methods=["GET"])
def statistics_index():
    return render_template("statistics/mainstats.html", top10_threads=Thread.find_top10_threads(), threadcount=Thread.query.count())