from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

pupil_list = [{"id": 1,
    "name": "Aasmund",
    "grade": 1
    },
    {
    "id": 3,
    "name": "Preben",
    "grade": 6
    }
    ]

@app.route("/")
def index():
    return "hello world"

# py -m flask run, dette må skrives i terminalen for å kjøre koden

@app.route("/pupils")
def get_pupils():\
    return jsonify(pupil_list)

@app.route("/pupils/<id>")
def get_pupil(id=None):
    for pupil in pupil_list:
        if str(pupil["id"]) == id:
            return jsonify(pupil)
    return jsonify(f"You requested the pupil with id {id}, but it did not exist")

@app.route("/search")
def search():
    return f"Your request args: {dict(request.args)}"

@app.route("/<animal_input>")
def get_animal(animal_input=None):
    with open("list-animals-world-611j.csv", "r") as csv_file:
        animals = csv.DictReader(csv_file)
        for animal in animals:
            if animal["Animal"].lower() == animal_input.lower():
                return animal
        return "Could not find animal"

# python app.py

if __name__ == "__main__":  
    app.run(debug=True)