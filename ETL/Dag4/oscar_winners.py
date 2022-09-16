# 1. Create a table oscar_winners with the following schema using the psycopg2 package

import csv
import psycopg2


# cur.execute("DROP TABLE oscar_winners;")
# conn.commit()
# cur.close()

def create_table():
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE oscar_winners (id serial PRIMARY KEY, year integer, age integer, name varchar, movie varchar);")
            conn.commit()


# create_table()

# 3. Create a function get_youngest_oscar_winner() that queries the database and returns the name, year, age and movie of the youngest oscar winner.

def get_youngest_oscar_winner():
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name, year, age, movie FROM oscar_winners ORDER BY age;")
            youngest = cur.fetchone()
            return youngest

# get_youngest_oscar_winner()

# 4. Create a function get_winners_by_age(age) that has age as a parameter, queries the database for all oscar winners that are that age and returns them as a list of lists.

def get_winners_by_age(age):
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            winners_by_age = []
            cur.execute("SELECT * FROM oscar_winners WHERE age = %s;", [age])
            for row in cur:
                winners_by_age.append(list(row))
            return winners_by_age

# get_winners_by_age(37)

# 5. Create a function `get_winners_by_name(name)` that has name as a paramater and returns all oscar winners in the database that has a name that contains the given name. 

def get_winners_by_name(name):
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            name = '%' + name + '%'
            winners_by_name = []
            cur.execute("SELECT name FROM oscar_winners WHERE name LIKE %s;", [name])
            for row in cur:
                winners_by_name.append(row[0].strip())
            return winners_by_name

# get_winners_by_name("Robert")

# 6. Create a function `multiple_oscar_winners(num_oscars)` that returns a dict of all oscar winners that has won `num_oscars` or more Oscars.

def multiple_oscar_winners(num_oscars):
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            multiple_winners = {}
            cur.execute("SELECT name, count(name) FROM oscar_winners GROUP BY name HAVING count(name) >= %s;", [num_oscars])
            for row in cur:
                multiple_winners[row[0]] = row[1]
            return multiple_winners

# multiple_oscar_winners(2)

# 7. If you have looked at the data closely, you might notice that the Oscar winners in this list only go to 2016! 
# Create a function `write_oscar_winner(name, age, year, movie)` that writes a new row to the database. 
# Use it to fill in the years 2017-2022 (You can do random names and movies if you don't feel like looking up who won the last six years ;))

def write_oscar_winner(name, age, year, movie):
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO oscar_winners (name, age, year, movie) VALUES (%s, %s, %s, %s);", [name, age, year, movie])
            conn.commit()

# write_oscar_winner("Casey Affleck", 43, 2017, "Manchester by the Sea")
# write_oscar_winner("Frances McDormand", 59, 2018, "Three Billboards outside Ebbing, Missouri")
# write_oscar_winner("Rami Malek", 36, 2019, "Bohemian Rhapsody")
# write_oscar_winner("Joaquin Phoenix", 42, 2020, "Joker")
# write_oscar_winner("Anthony Hopkins", 82, 2021, "The Father")
# write_oscar_winner("Will Smith", 53, 2022, "King Richard")


# 8. You might also have noticed that this is only the best male actors that have won an Oscar.
# Download the file `female_oscar_winners.csv`, but this time you are not allowed to use the DBEaver import function to insert them to the database!
# Use the `csv` library together with the necessary functions you created in the tasks above.

def import_csv_file(file):
    with psycopg2.connect("dbname=postgres user=postgres password=mysecretpassword", port=5544) as conn:
        with conn.cursor() as fp:
            with open(file, "r") as fp:
                oscar_age_female = csv.DictReader(fp)
                for row in oscar_age_female:
                    name = row[' "Name"'].strip().strip('"')
                    age = row[' "Age"'].strip()
                    year = row[' "Year"'].strip()
                    movie = row[' "Movie"'].strip().strip('"')
                    write_oscar_winner(name, age, year, movie)
            conn.commit()

# import_csv_file("oscar_age_female.csv")


# 9. Congrats! You made it to the end. (Almost). Can you plug the functionality you just created into an api? For instance, try to create an API endpoint 
# per function you created above. (For the `write_oscar_winner` function you will need to do a POST request)
