import requests

# Function that takes in origin, destination, flightclass and passengers as parameters and returns a json file 
# with co2 emissions for this flight.

def get_flight_emission_estimate(origin:str, destination:str, flightclass:str="first", passengers:int=2) -> dict:
    """Get co2 emission pr passenger for ONE flight, from airport to destination. 

    Args:
        origin (str): Airport code f.ex "BER"
        destination (str): Airport code f.ex "HAM"
        flightclass (str, optional): Flight class. Can be "unknown", "economy", "business" or "first". Defaults to "first".
        passengers (int, optional): Amount of passengers. Defaults to 2.

    Returns:
        dict: json
    """
    MY_API_KEY="N0WVKZJFHV429JN00Q6EVRJVPCAK"
    url = "https://beta3.api.climatiq.io/travel/flights"

    json_body = {
        "legs": [{
            "from": origin,
            "to": destination,
            "passengers": passengers,
            "class": flightclass
        }]
    }

    authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}
    response = requests.post(url, json=json_body, headers=authorization_headers).json()

    return response

# A function that takes in flights as a list with dictionaries and returns the co2 emissions
# for every flight.

def get_flights_emission_estimate(flights:list) -> dict:
    """Get co2 emission pr passenger for a list of dicts of flights, from airport to destination. 

    Args:
        flights = list of dicts.

        Example:
        [
        {
            "from": "BER",
            "to": "HAM",
            "passengers": 2,
            "class": "first"
        },
        {
            "from": "HAM",
            "to": "JFK",
            "passengers": 2,
            "class": "economy"
        }
        ]

    Returns:
        dict: json
    """
    MY_API_KEY="N0WVKZJFHV429JN00Q6EVRJVPCAK"
    url = "https://beta3.api.climatiq.io/travel/flights"

    json_body = {
        "legs": flights
    }

    authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}
    response = requests.post(url, json=json_body, headers=authorization_headers).json()

    return response
