from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.models import Bike, User, Rental
from collections import namedtuple


@app.route('/')
@app.route('/index')
def hello():
    key = app.config['GOOGLE_API_KEY']
    bikes = Bike.query.all()
    return render_template('index.html', bikes=bikes, key=key)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
