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
    if "user" not in session:
        flash("You need to log in to add an activity!")
        return redirect(url_for("login"))

    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())
    if request.method == "POST":
        activity = Activity(
            activity_name=request.form.get("activity_name"),
            activity_description=request.form.get("activity_description"),
            activity_age=request.form.get("activity_age"),
            activity_type=request.form.get("activity_type"),
            activity_developmental=request.form.get("activity_developmental"),
            activity_createdby=session.get("user"),
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
         
    if "user" not in session:
        flash("You need to log in to edit an activity!")
        return redirect(url_for("login"))
    
    if activity.activity_createdby != session["user"]:
        flash("You can only edit your own activities!")
        return redirect(url_for("activities"))

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
    if activity.activity_createdby != session["user"]:
        flash("You can only delete your own activities!")
        return redirect(url_for("activities"))
    else:
        db.session.delete(activity)
        db.session.commit()
    return redirect(url_for("activities"))


@app.route("/occasions")
def occasions():
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())
    return render_template("occasions.html", occasions=occasions)


@app.route("/add_occassion", methods=["GET", "POST"])
def add_occasion():
    if "user" not in session:
        flash("You need to log in to add an occasion!")
        return redirect(url_for("login"))

    if request.method == "POST":
        occasion = Occasion(
            occasion_name=request.form.get("occasion_name"),
            occasion_createdby=session.get("user"),)
        db.session.add(occasion)
        db.session.commit()
        return redirect(url_for("occasions"))
    return render_template("add_occasion.html")


@app.route("/edit_occassion/<int:occasion_id>", methods=["GET", "POST"])
def edit_occasion(occasion_id):
    occasion = Occasion.query.get_or_404(occasion_id)

    if "user" not in session:
        flash("You need to log in to edit an occasion!")
        return redirect(url_for("login"))
    
    if occasion.occasion_createdby != session["user"]:
        flash("You can only edit your own occasions!")
        return redirect(url_for("occasions"))

    if request.method == "POST":
        occasion.occasion_name = request.form.get("occasion_name")
        db.session.commit()
        return redirect(url_for("occasions"))
    return render_template("edit_occasion.html", occasion=occasion)


@app.route("/delete_occasion/<int:occasion_id>")
def delete_occasion(occasion_id):
    occasion = Occasion.query.get_or_404(occasion_id)
    if occasion.occasion_createdby != session["user"]:
        flash("You can only delete your own occasions!")
        return redirect(url_for("occasions"))
    else:
        db.session.delete(occasion)
        db.session.commit()
    return redirect(url_for("occasions"))


@app.route("/activities_by_occasion/<int:occasion_id>")
def activities_by_occasion(occasion_id):
    activities = list(Activity.query.order_by(Activity.activity_name).all())
    occasion = Occasion.query.get_or_404(occasion_id) 
    return render_template("activities_by_occasion.html", 
                           occasion=occasion, activities=activities, occasions=occasions)


@app.route("/age-groups")
def age_groups():
    ages = ["12 months", "12-18 Months", "18-24 Months", "2-3 Years", "3-5 Years", "5-7 Years", "7-11 Years" ,"11+ Years"]
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
        return render_template("profile.html", username=session["user"])

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
                    flash("Click on your username to load profile")
                    return render_template("profile.html", username=session["user"])
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    activities = list(Activity.query.order_by(Activity.activity_name).all())
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())
    if "user" in session:
        return render_template("profile.html", username=session["user"], activities=activities, occasions=occasions)   
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))



