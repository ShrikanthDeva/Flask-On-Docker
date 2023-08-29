# creating new flask app and configuring first route
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy


# create the app
app = Flask(__name__)
# configure the postgres db, relative to the app instance
app.config.from_object('project.config.Config')
# create the extension
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email




@app.route("/")
def hello_world():
    return jsonify(hello="world")
