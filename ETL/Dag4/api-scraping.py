import psycopg2
import requests
import json


def retrieve_resource(url):
    response = requests.get(url)
    return response

def create_table_films():
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE films (
                "film_id" serial PRIMARY KEY,
                "title" varchar,
                "episode_id" integer,
                "opening_crawl" varchar,
                "director" varchar,
                "producer" varchar,
                "release_date" varchar,
                "characters" varchar array,
                "planets" varchar array,
                "starships" varchar array,
                "vehicles" varchar array,
                "species" varchar array,
                "url" varchar,
                "created" varchar,
                "edited" varchar
            )""")
            conn.commit()

def create_table_person():
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE person (
                "person_id" serial PRIMARY KEY,
                "name" varchar,
                "height" varchar,
                "mass" varchar,
                "hair_color" varchar,
                "skin_color" varchar,
                "eye_color" varchar,
                "birth_year" varchar,
                "gender" varchar,
                "homeworld" varchar,
                "films" varchar array,
                "species" varchar array,
                "vehicles" varchar array,
                "starships" varchar array,
                "url" varchar,
                "created" varchar,
                "edited" varchar
                )""")
            conn.commit()

def create_table_films_people():
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE films_person (
                "film_id" int unique,
                "person_id" int unique,
                PRIMARY KEY("film_id", "person_id"),
                FOREIGN KEY("film_id") REFERENCES films("film_id"),
                FOREIGN KEY("person_id") REFERENCES person("person_id")
                )""")
            conn.commit()

create_table_person()
create_table_films_people()