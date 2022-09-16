# %%
import requests
from PIL import Image

base_url = "https://pokeapi.co/api/v2"
end_point = "/pokemon"

# %%
def get_pokemons():
    response = requests.get(base_url+end_point)
    if response.ok:
        return response.json()["results"]

# %%
def get_pokemon_sprites():
    pokemons = get_pokemons()
    sprites = {}
    for pokemon in pokemons:
        response = requests.get(pokemon["url"])
        if response.ok:
            json_data = response.json()
            sprites[pokemon["name"]] = json_data["sprites"]["front_default"]
    return sprites

print(get_pokemon_sprites())

# %%
def write_pokemon_sprites_to_files():
    sprites = get_pokemon_sprites()
    for k,v in sprites.items():
        url = v
        with open(k + '.png', 'wb') as handler:
            response = requests.get(url)
            handler.write(response.content)

write_pokemon_sprites_to_files()
        

# %%
def show_pokemon_sprite(pokemon):
    sprites = get_pokemon_sprites()
    return sprites[pokemon]

show_pokemon_sprite('bulbasaur')

# %%



