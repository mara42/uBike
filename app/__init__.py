import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bikesdatabase.db"))

app = Flask(__name__, static_url_path='', 
            static_folder='templates/static')

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SECRET_KEY'] = 'AJABJHGJKHDFGSKJHJDALKEILXNKAB'

api_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "google_api.txt")
if os.path.exists(api_path):
    with open(api_path, 'r') as f:
        g_api = f.read()
else:
    raise FileNotFoundError("need google api key")

app.config['GOOGLE_API_KEY'] = g_api
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app import routes
