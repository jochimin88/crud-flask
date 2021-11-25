from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI


app = Flask(__name__)


app.secret_key = "jochimin"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)


app.register_blueprint(contacts)
