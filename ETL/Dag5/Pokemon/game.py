import psycopg2
from random import randint

def get_random_pokemon():
    index = randint(0,19)
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM pokemons")
            for row in cur:
                if row[0] == index:
                    return row

def get_pokemon(pokemon):
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM pokemons")
            for row in cur:
                if row[1] == pokemon:
                    return row

comp_choice = get_random_pokemon()
player_choice = get_pokemon('bulbasaur')




