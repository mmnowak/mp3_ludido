from flask import Flask, render_template, request, redirect, url_for, flash, session
from ludido import app, db
from ludido.models import Occasion, Activity, Users
from werkzeug.security import generate_password_hash, check_password_hash


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
    if request.method == 'POST':
    # check if username already exists in db
        existing_user = Users.query.filter(Users.username == \
                                           request.form.get("username").lower()).all()
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = Users(
            username = request.form.get("username").lower(),
            password = generate_password_hash(request.form.get("password"))
            )
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!")
        return redirect(url_for("index", username=session["user"]))


    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = Users.query.filter(Users.username == \
                                           request.form.get("username").lower()).all() 

        if existing_user:
            if check_password_hash(
                existing_user[0].password, request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")
