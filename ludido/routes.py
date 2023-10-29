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
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())
    if request.method == "POST":
        activity = Activity(
            activity_name=request.form.get("activity_name"),
            activity_description=request.form.get("activity_description"),
            activity_age=request.form.get("activity_age"),
            activity_type=request.form.get("activity_type"),
            activity_developmental=request.form.get("activity_developmental"),
            occasion_id=request.form.get("occasion_id")
            )
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for("activities"))
    return render_template("add_activity.html", occasions=occasions)


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


@app.route("/edit_occassion/<int:occasion_id>", methods=["GET", "POST"])
def edit_occasion(occasion_id):
    occasion = Occasion.query.get_or_404(occasion_id)
    if request.method == "POST":
        occasion.occasion_name = request.form.get("occasion_name")
        db.session.commit()
        return redirect(url_for("occasions"))
    return render_template("edit_occasion.html", occasion=occasion)


@app.route("/delete_occasion/<int:occasion_id>")
def delete_occasion(occasion_id):
    occasion = Occasion.query.get_or_404(occasion_id)
    db.session.delete(occasion)
    db.session.commit()
    return redirect(url_for("occasions"))