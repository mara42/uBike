from app import app
import flask
from flask import render_template
from app.forms import LoginForm
from flask_login import login_user


@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html', title='uBike')


@app.route('/login')
def login_page():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        print(form)
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)
