from app import app
import flask
from flask_login import login_user
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
        ) for i in range(20)
    ]
    return render_template("index.html", bikes=bikes, key=key, center=center)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/rental", methods=["GET", "POST"])
def rental():
    return render_template("rental.html")


# @app.route('/login')
# def login_page():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)

# @app.route('/login', methods=['POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         print(form)
#         login_user(user)

#         flask.flash('Logged in successfully.')

#         next = flask.request.args.get('next')
#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)
