from flask import Flask, render_template, request, redirect, url_for
from ludido import app, db
from ludido.models import Occasion, Activity


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/activities")
def activities():
    activities = list(Activity.query.order_by(Activity.activity_name).all())
    return render_template("activities.html", activities=activities)


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


@app.route("/full_activity/<int:activity_id>")
def full_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    return render_template("full_activity.html", activity=activity)


@app.route("/edit_activity/<int:activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())
    if request.method == "POST":
        activity.activity_name = request.form.get("activity_name"),
        activity.activity_description = \
            request.form.get("activity_description"),
        activity.activity_age = request.form.get("activity_age"),
        activity.activity_type = request.form.get("activity_type"),
        activity.activity_developmental = \
            request.form.get("activity_developmental"),
        activity.occasion_id = request.form.get("occasion_id")
        db.session.commit()
        return redirect(url_for("activities"))
    return render_template("edit_activity.html", activity=activity, 
                           occasions=occasions)


@app.route("/delete_activity/<int:activity_id>")
def delete_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for("activities"))


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


@app.route("/activities_by_occasion/<int:occasion_id>")
def activities_by_occasion(occasion_id):   
    occasion = Occasion.query.get_or_404(occasion_id) 
    activities = list(Activity.query.filter_by(occasion).all())
    return render_template("activities_by_occasion.html",
                           activities=activities)


@app.route("/age-groups")
def age_groups():
    return render_template("age-groups.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'confirm-password' in request.form:
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['password']


    return render_template("register.html")

