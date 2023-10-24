from flask import render_template
from ludido import app, db

@app.route("/")
def home():
    return render_template("base.html")