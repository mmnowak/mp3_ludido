from flask import render_template
from ludido import app, db
from ludido.models import Ages, Type, Development, Occasion, Activity


@app.route("/")
def home():
    return render_template("base.html")