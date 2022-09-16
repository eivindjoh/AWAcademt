import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    response = requests.request("GET", url)
    if response.ok:
        return response.text



