import json
from flask import Flask, render_template, request, redirect, \
                    url_for, flash, session
from ludido import app, db
from ludido.models import Occasion, Activity, Users, Favourite
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def index():
    """
    Function to render the index html page
    """
    return render_template("index.html")


@app.route("/activities")
def activities():
    """
    Function that will display all the activities added to the DB by users,
    and either add or remove from favourites if the user is logged in
    """
    favourites = list(Favourite.query.order_by(Favourite.activity_id).all())
    activities = list(Activity.query.order_by(Activity.activity_name).all())
    activity_id = Activity.id
    return render_template("activities.html", activities=activities,
                           favourites=favourites)


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    """
    Function that checks if the user is logged in, then if
    the chosen name already exists, then add the new activity to the DB
    """
    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to add an activity!")
        return redirect(url_for("login"))

    """
    Loads occasions added to the DB by users and inserts into the form
    """
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())

    if request.method == "POST":
        """
        Checks if an activity with the name inputed already exists
        """
        existing_activity = \
            Activity.query.filter(Activity.activity_name ==
                                  request.form.get("activity_name")).all()
        if existing_activity:
            flash("An activity with this name already exists!")
            return redirect(url_for("add_activity"))

        """
        Adds a new activity to the DB
        """
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
    """
    Renders a page displaying all the activity details
    """
    activity = Activity.query.get_or_404(activity_id)
    return render_template("full_activity.html", activity=activity)


@app.route("/full_activity/<int:activity_id>/favourite", methods=["POST"])
def add_favourite(activity_id):
    """
    Function that checks if the user is logged in,
    then if the activity is already
    in favourites, then adds a new favourite into the DB
    """
    activity = Activity.query.get_or_404(activity_id)

    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to add to favourites!")
        return render_template("full_activity.html", activity=activity)

    if request.method == "POST":
        """
        Checks if the activity is already in favourites
        """
        is_favourite = Favourite.query.filter(Favourite.activity_id
                                              == activity_id).first()
        if is_favourite:
            flash("Already in favourites!")
            return redirect(url_for("activities"))
        else:
            # Adds a new favourite activity to the DB            
            favourite = Favourite(
                username=session.get("user"),
                activity_id=activity_id
                )

            # adds user favourite to db
            db.session.add(favourite)
            db.session.commit()
            flash("Added to favourites!")

    return render_template("full_activity.html", activity=activity)


@app.route("/full_activity/<int:activity_id>/unfavourite")
def remove_favourite(activity_id):
    """
    Checks if the user is logged in, then if activity is in favourites,
    it yes it removes the favourite activity from the DV
    """
    activity = Activity.query.get_or_404(activity_id)
    activities = list(Activity.query.order_by(Activity.id).all())
    favourites = list(Favourite.query.order_by(Favourite.username).all())

    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to do this!")
        return render_template("full_activity.html", activity=activity)
    else:
        username = session["user"]

    """
    Removes the favourite activity from the DB for the user
    """
    for favourite in favourites:
        if username == favourite.username and \
         activity.id == favourite.activity_id:
            # removes user favourite from db
            db.session.delete(favourite)
            db.session.commit()
            flash("Removed from favourites!")
            return redirect(url_for("activities"))

    return render_template("favourite_activities.html",
                           activities=activities, favourites=favourites,
                           username=session["user"])


@app.route("/favourite-activities/<username>/unvafourite_all")
def unfavourite_all(username):
    """
    Function that lets logged in users
    remove all activities from their favourites
    """
    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to do this!")
        return redirect(url_for("login"))
    else:
        username = session["user"]

    activities = list(Activity.query.order_by(Activity.id).all())
    favourites = list(Favourite.query.order_by(Favourite.username).all())

    for favourite in favourites:
        """
        Removes all favourite activities from the DB for the ser
        """
        if username == favourite.username:
            # removes all user favourites from db
            db.session.delete(favourite)
            db.session.commit()

    flash("Removed all favourites!")
    return redirect(url_for("activities"))


@app.route("/favourite-activities/<username>")
def favourite_activities(username):
    """
    Displays favourite activities for the user
    """

    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to see your favourites!")
        return redirect(url_for("activities"))
    else:
        username = session["user"]

    activities = list(Activity.query.order_by(Activity.id).all())
    favourites = list(Favourite.query.order_by(Favourite.username).all())
    return render_template("favourite_activities.html",
                           activities=activities, favourites=favourites,
                           username=session["user"])


@app.route("/edit_activity/<int:activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    """
    Function that allows user edit the activities they have added
    """
    activity = Activity.query.get_or_404(activity_id)
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())

    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to edit an activity!")
        return redirect(url_for("login"))

    if activity.activity_createdby != session["user"]:
        """
        Checks if the user is trying to edit their own activity
        """
        flash("You can only edit your own activities!")
        return redirect(url_for("activities"))

    if request.method == "POST":
        """
        Checks if an activity with the name inputed already exists
        """
        existing_activity = \
            Activity.query.filter(Activity.activity_name ==
                                  request.form.get("activity_name")).all()
        if existing_activity:
            flash("An activity with this name already exists!")
            return redirect(url_for("edit_activity"))

        """
        Handle the form submission with the updated data
        """
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
    """
    Function that lets user delete activity they have created
    """
    activity = Activity.query.get_or_404(activity_id)
    if activity.activity_createdby != session["user"]:
        """
        Checks if the user is trying to delete their own activity
        """
        flash("You can only delete your own activities!")
        return redirect(url_for("activities"))
    else:
        """
        Delete the activity from the DB
        """
        db.session.delete(activity)
        db.session.commit()
        flash("You deleted the activity!")
    return redirect(url_for("activities"))


@app.route("/occasions")
def occasions():
    """
    Displays all the occasions added by users
    """
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())
    return render_template("occasions.html", occasions=occasions)


@app.route("/add_occassion", methods=["GET", "POST"])
def add_occasion():
    """
    Function that checks if the user is logged in,
    then if an occasion already exists,
    then adds a new occasion to the DB
    """

    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to add an occasion!")
        return redirect(url_for("login"))

    if request.method == "POST":
        """
        Checks if the name chosen already exists
        """
        existing_occasion = Occasion.query.filter(Occasion.occasion_name
                                                  == request.form.get(
                                                      ("occasion_name")).all())
        if existing_occasion:
            flash("An occasion with this name already exists!")
            return redirect(url_for("add_occasion"))

        """
        Handle the form submission and adds a new occasion to the DB
        """
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
    """
    Function that checks if the user is logged in and if
    they have created the occasion; if yes, amends
    the occasion in the DB
    """
    occasion = Occasion.query.get_or_404(occasion_id)

    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to edit an occasion!")
        return redirect(url_for("login"))

    if occasion.occasion_createdby != session["user"]:
        """
        Checks if the user is editing their own occasion
        """
        flash("You can only edit your own occasions!")
        return redirect(url_for("occasions"))

    if request.method == "POST":
        """
        Handles the form submission and amends the occasion in the DB
        """
        occasion.occasion_name = request.form.get("occasion_name")
        db.session.commit()
        flash("You edited the occasion!")
        return redirect(url_for("occasions"))
    return render_template("edit_occasion.html", occasion=occasion)


@app.route("/delete_occasion/<int:occasion_id>")
def delete_occasion(occasion_id):
    """
    Checks if the user is logged in, then if they are deleting
    their own occasion, if yes removes the occasion
    from the DB
    """
    occasion = Occasion.query.get_or_404(occasion_id)

    if "user" not in session:
        """
        Checks if the user is logged in
        """
        flash("You need to log in to delete an occasion!")
        return redirect(url_for("login"))

    if occasion.occasion_createdby != session["user"]:
        """
        Checks if the user is deleting their own occasion
        """
        flash("You can only delete your own occasions!")
        return redirect(url_for("occasions"))
    else:
        # Removes the occasion from the DB
        db.session.delete(occasion)
        db.session.commit()
        flash("You deleted the occasion!")
    return redirect(url_for("occasions"))


@app.route("/activities_by_occasion/<int:occasion_id>")
def activities_by_occasion(occasion_id):
    # Displays the activities for the selected occasion
    activities = list(Activity.query.order_by(Activity.activity_name).all())
    favourites = list(Favourite.query.order_by(Favourite.activity_id).all())
    occasion = Occasion.query.get_or_404(occasion_id)
    return render_template("activities_by_occasion.html",
                           occasion=occasion, activities=activities,
                           occasions=occasions, favourites=favourites)


@app.route("/age-groups")
def age_groups():
    # Retrieves and displays data from the JSON file
    data = []
    with open("ludido/data/ages.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("age-groups.html", ages=data)


@app.route("/activities_by_age/<age_id>")
def activities_by_age(age_id):
    """
    Retrieves the age groups data from the JSON file
    and displays activities and information for the selected age group
    """
    age = {}
    with open("ludido/data/ages.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["age_id"] == age_id:
                age = obj
                print(age)

    activities = list(Activity.query.order_by(Activity.activity_name).all())
    favourites = list(Favourite.query.order_by(Favourite.activity_id).all())
    return render_template("activities_by_age.html", age=age,
                           activities=activities, favourites=favourites)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function that lets users register a new account. First it checks
    if the chosen username already exists, then if the password and the confirm
    passwords match, then adds user details
    including a hashed password to the DB
    """
    if request.method == 'POST':
        # check if username already exists in db
        existing_user = \
         Users.query.filter(Users.username ==
                            request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if request.form.get("password") != \
           request.form.get("confirm_password"):
            # Checks if the password and the confirmed passwords match
            flash("Passwords do not match!")
            return redirect(url_for("register"))

        # Handles the form submission and adds a new user to the DB
        user = Users(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
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
    """
    Function that lets the user log in. First it checks if the username exists,
    then if the username and password match
    """
    if request.method == "POST":
        # Checks if the username exists
        existing_user = \
         Users.query.filter(Users.username ==
                            request.form.get("username").lower()).all()

        if existing_user:
            if check_password_hash(existing_user[0].password,
                                   request.form.get("password")):
                # Checks if the username and the password match
                session["user"] = request.form.get("username").lower()
                flash("Click on your username to load profile")
                return render_template("profile.html",
                                       username=session["user"])
            else:
                # Informs user they have input the wrong data
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # Informs user they have input the wrong data
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    A function that displays the user's name
    and activities and occasions they have created
    """
    activities = list(Activity.query.order_by(Activity.activity_name).all())
    occasions = list(Occasion.query.order_by(Occasion.occasion_name).all())
    if "user" in session:
        """
        Checks if the user is logged in, retrieves their username
        and displays their profile
        """
        return render_template("profile.html", username=session["user"],
                               activities=activities, occasions=occasions)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Function that clears all session data to log the user out
    and redirect to the log in page
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.errorhandler(404)
def not_found(e):
    # Function which displays a custom error 404 page
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(e):
    # Function which displays a custom error 500 page
    return render_template("500.html"), 500


@app.errorhandler(403)
def error_forbidden(e):
    # Function which displays a custom error 403 page
    return render_template("403.html"), 500
