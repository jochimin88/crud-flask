# imports
from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect
from models.contacts import Contact

from utils.db import db


contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)
    return render_template("index.html")


@contacts.route("/new", methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]
    

    new_contact = Contact(fullname, email, phone)
    
    db.session.add(new_contact)
    db.session.commit()

    flash("Contact added!")
   
    return redirect(url_for("contacts.index"))

@contacts.route("/update/<id>", methods = ['POST', 'GET'])
def update(id):
    contact = Contact.query.get(id)
    
    if request.method == 'POST':
        
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]

        db.session.commit()

        flash("Contact updated!")
        return redirect(url_for("contacts.index"))
        
    return render_template('update.html',contact=contact)
        

@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash("Contact deleted!")
    
    return redirect(url_for("contacts.index"))
    #return {"message": "delete contact"}

    


# about route
@contacts.route("/about")
def about():
    return render_template("about.html")

