from flask import Flask, send_file
from pokemon import show_pokemon_sprite

app = Flask(__name__)

@app.route("/")
def index():
    return "Velkommen til mitt Pokemon-API"

@app.route("/<pokemon>")
def get_image(pokemon):
    filename = pokemon + '.png'
    return send_file(filename, mimetype='image/png')


if __name__ == "__main__":  
    app.run(debug=True)