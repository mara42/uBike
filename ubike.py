from app import app
from flask import render_template


@app.route('/')
def hello():
    return render_template('index.html', title='uBike')


if __name__ == '__main__':
    app.app.run()