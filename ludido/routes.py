from flask import render_template, request, redirect, url_for
from ludido import app, db
from ludido.models import Occasion, Activity


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/activities")
def activities():
    return render_template("activities.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    if request.method == "POST":
        activity = Activity(activity_name=request.form.get("activity_name"))
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for("activities"))
    return render_template("add_activity.html")


@app.route("/occasions")
def occasions():
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())
    return render_template("occasions.html", occasions=occasions)


@app.route("/add_occassion", methods=["GET", "POST"])
def add_occasion():
    if request.method == "POST":
        occasion = Occasion(occasion_name=request.form.get("occasion_name"))
        db.session.add(occasion)
        db.session.commit()
        return redirect(url_for("occasions"))
    return render_template("add_occasion.html")