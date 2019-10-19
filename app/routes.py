from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.models import Bike, User, Rental
from collections import namedtuple
import random


FBike = namedtuple("Bike", ["id", "lat", "lng"])


@app.route("/")
@app.route("/index")
def hello():
    key = app.config["GOOGLE_API_KEY"]
    # bikes = Bike.find_free_bikes()
    center = (55.859703, -4.2531847)
    bikes = [
        FBike(
            i,
            center[0] + random.randint(-50, 50) * 1e-04,
            center[1] + random.randint(-50, 50) * 1e-04,
        )
        for i in range(20)
    ]
    return render_template("index.html", bikes=bikes, key=key, center=center)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
