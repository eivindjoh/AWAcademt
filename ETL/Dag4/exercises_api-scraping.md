# Exercises - API consumption

## Useful links

- The [Star Wars API](https://swapi.dev/) (swapi.dev)
- The [Request module](https://docs.python-requests.org/en/master/) (docs.python-requests.org)

## Setup

1. You need to install the `requests` module and the `psycopg2` module in your python virtualenv:
   1. `python -m pip install requests`
   1. `python -m pip install psycopg2` If `psycopg2` doesn't work, then try to install `psycopg2-binary`.
2. You need to have access to a postgres server. Either the one you have installed on your Windows machine, or a server running inside a docker container.

Please note for this exercise that the SWAPI is limited to 10,000 requests for a given day for a given IP address. Make sure to not exeed that number.

## Exercise 1 - Familiarize yourself with the API and the docs

1. Familiarise yourself with the SWAPI using the tool in the front page. Look at the responses, build a sense of how the data is structured and how it can be scraped.
2. Skim throught the documentation page [link here](https://swapi.dev/documentation).
3. Write a Python function that retrieves a single resource from the SWAPI given its resource URL, and returns the response object.

## Exercise 2 - Parse the schemas

1. Try to use the function above to run `/schema/` for all resource types in the SWAPI (f.ex. `/people/schema/`). Check out a description of schemas [here](https://swapi.dev/documentation#schema). If this doesn't work, you need to parse the schema by hand. For each resourse type (e.g. people), use a resourse you think has a complete number of attributes.

## Exercise 3 - Create tables per resource type

1. Create a new database for these exercises.
1. For each resource type, create corresponding tables in your new database by using the schema you have started parsing. If you have to do the schema parsing manually, you will probably need to iterate multiple times here.

## Exercise 3 - Function to populate

5. For each resource type (e.g. planets), write a Python function to populate the corresponding table based on a response object.
6. Try it out! Can you populate at least one resource in each table?

## Bonuse exercise - Scraping the entire API

1. Write a Python program that scrapes the entire API, starting with only the information in the Luke Skywalker resource. Ensure that your program never requests the same resource more than once. Discuss with a classmate how you should build your program before you start writing any code.
2. Find some interesting statistics about the Star Wars universe based on your brand new database!

## Bonus exercise - Automize creation of resource type tables

1. Consider task 3 again. Can you figure out a way to create a function that accepts the path to a resource schema, and creates the table for the resource type in the database without any further user intervention?
