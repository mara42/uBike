from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html', title='uBike')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
