#!/bin/python3

from flask import Flask, render_template, abort

app = Flask(__name__)


"""Information regarding the Pets in the System."""
Pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
        ]

@app.route("/")
def home():
    return render_template("home.html",pets = Pets)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<my_name>")
def greeting(my_name):
    return "Welcome " + my_name + "!"

@app.route("/square/<int:number>")
def show_square(number):
    return "Square of " + str(number) + " is: " + str(number*number)

@app.route("/template")
def showTemplate():
    return render_template("home.html")

@app.route("/details/<int:pet_id>")
def petDetails(pet_id):
    pet = next((pet for pet in Pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet = pet)

if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1", port = 3000)
