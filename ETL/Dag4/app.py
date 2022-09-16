from flask import Flask, jsonify, request
import oscar_winners

app = Flask(__name__)


@app.route("/youngest")
def youngest():
    return jsonify(oscar_winners.get_youngest_oscar_winner())

@app.route("/age/<age>")
def byage(age):
    return jsonify(oscar_winners.get_winners_by_age(age))


if __name__ == "__main__":  
    app.run(debug=True)