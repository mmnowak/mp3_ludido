import json
from flask import Flask, render_template, request, redirect, url_for, flash, session
from ludido import app, db
from ludido.models import Occasion, Activity, Users, Favourite
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/activities")
def activities():
    favourites = list(Favourite.query.order_by(Favourite.activity_id).all()) 
    activities = list(Activity.query.order_by(Activity.activity_name).all())
    activity_id = Activity.id
    return render_template("activities.html", activities=activities, favourites=favourites)


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
            existing_activity = Activity.query.filter(Activity.activity_name == \
                                           request.form.get("activity_name")).all()
            if existing_activity:
                flash("An activity with this name already exists!")
                return redirect(url_for("add_activity"))

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
            flash("Thank you for adding a new activity!")
            return redirect(url_for("activities"))

    return render_template("add_activity.html", occasions=occasions)    


@app.route("/full_activity/<int:activity_id>")
def full_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    return render_template("full_activity.html", activity=activity)


@app.route("/full_activity/<int:activity_id>/favourite", methods=["POST"])
def add_favourite(activity_id):
    activity = Activity.query.get_or_404(activity_id)

    if "user" not in session:
        flash("You need to log in to add to favourites!")
        return render_template("full_activity.html", activity=activity)

    if request.method == "POST":

        is_favourite = Favourite.query.filter(Favourite.activity_id == activity_id).first() 
        if is_favourite:
            flash("Already in favourites!")
            return redirect(url_for("activities"))
        
        favourite = Favourite(
        username = session.get("user"),
            activity_id = activity_id
            )
        flash("Added to favourites!")
    
        # adds user favourite to db
        db.session.add(favourite)
        db.session.commit()
        print(favourite)   

    return render_template("full_activity.html", activity=activity)


@app.route("/full_activity/<int:activity_id>/unfavourite")
def remove_favourite(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    activities = list(Activity.query.order_by(Activity.id).all())
    favourites = list(Favourite.query.order_by(Favourite.username).all ()) 

    if "user" not in session:
        flash("You need to log in to do this!")
        return render_template("full_activity.html", activity=activity)
    else:
        username = session["user"]

    for favourite in favourites: 
        if username == favourite.username and activity.id == favourite.activity_id:
        # removes user favourite from db
            db.session.delete(favourite)
            db.session.commit()
            flash("Removed from favourites!")
            return redirect(url_for("activities"))
    
    return render_template("favourite_activities.html",
                           activities=activities, favourites=favourites, username=session["user"])


@app.route("/favourite-activities/<username>/unvafourite_all")
def unfavourite_all(username):
    if "user" not in session:
        flash("You need to log in to do this!")
        return redirect(url_for("login"))
    else:
        username = session["user"]
    
    activities = list(Activity.query.order_by(Activity.id).all())
    favourites = list(Favourite.query.order_by(Favourite.username).all()) 

    for favourite in favourites:
        if username == favourite.username: 
            # removes all user favourites from db
            db.session.delete(favourite)
            db.session.commit()
    
    flash("Removed all favourites!")
    return redirect(url_for("activities"))


@app.route("/favourite-activities/<username>")
def favourite_activities(username):
    if "user" not in session:
        flash("You need to log in to see your favourites!")
        return redirect(url_for("activities"))
    else:
        username = session["user"]
   
    activities = list(Activity.query.order_by(Activity.id).all())
    favourites = list(Favourite.query.order_by(Favourite.username).all()) 
    return render_template("favourite_activities.html", 
                           activities=activities, favourites=favourites, username=session["user"])



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
        flash("You edited the activity!")
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
        flash("You deleted the activity!")
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
        existing_occasion = Occasion.query.filter(Occasion.occasion_name == \
                                           request.form.get("occasion_name")).all()
        if existing_occasion:
            flash("An occasion with this name already exists!")
            return redirect(url_for("add_occasion"))

        occasion = Occasion(
            occasion_name=request.form.get("occasion_name"),
            occasion_createdby=session.get("user"),)
        db.session.add(occasion)
        db.session.commit()
        flash("Thank you for adding a new occasion!")
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
        flash("You edited the occasion!")
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
        flash("You deleted the occasion!")
    return redirect(url_for("occasions"))


@app.route("/activities_by_occasion/<int:occasion_id>")
def activities_by_occasion(occasion_id):
    activities = list(Activity.query.order_by(Activity.activity_name).all())
    favourites = list(Favourite.query.order_by(Favourite.activity_id).all()) 
    occasion = Occasion.query.get_or_404(occasion_id) 
    return render_template("activities_by_occasion.html", 
                           occasion=occasion, activities=activities, occasions=occasions, favourites=favourites)


@app.route("/age-groups")
def age_groups():
    data = []
    with open("ludido/data/ages.json", "r") as json_data:
        data = json.load(json_data) 
    return render_template("age-groups.html", ages=data)


@app.route("/activities_by_age/<age_id>")
def activities_by_age(age_id):
    age = {}
    with open("ludido/data/ages.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["age_id"] == age_id:
                age = obj
                print(age)
    
    activities = list(Activity.query.order_by(Activity.activity_name).all()) 
    favourites = list(Favourite.query.order_by(Favourite.activity_id).all()) 
    return render_template("activities_by_age.html", age=age, activities=activities, favourites=favourites)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
    # check if username already exists in db
        existing_user = Users.query.filter(Users.username == \
                                           request.form.get("username").lower()).all()
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        if request.form.get("password") != request.form.get("confirm_password"):
            flash("Passwords do not match!")
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

    
@app.errorhandler(404) 
def not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500) 
def internal_error(e):
    return render_template("500.html"),500



