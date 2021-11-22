from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

password = 'G2s~Dj{kK#7Ug>6rD{L'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost/contacts'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)


app.register_blueprint(contacts)
