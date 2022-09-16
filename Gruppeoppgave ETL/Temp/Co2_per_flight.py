from Flight_id import flight_id
from Co2emissions import get_flights_emission_estimate


def create_list_with_flights(flights:list) -> list:
    """Creates a list with flights with 1 passenger for each class in that flight.

    Args:
        flights (dict): ex. [{"flight_id": "A3757", "airport_dep": "OSL", "airport_arr": "ATH"}]

    Returns:
        list: ex. [
        {
            "from": "BER",
            "to": "HAM",
            "passengers": 1,
            "class": "first"
        },
        {
            "from": "BER",
            "to": "HAM",
            "passengers": 1,
            "class": "business"
        }
        ]
    """
    flights_parameters = []
    for flight in flights:
        flightclasses = ["unknown", "economy", "business", "first"]
        for flightclass in flightclasses:
            departure = flight["airport_dep"]
            arrival = flight["airport_arr"]
            passengers = 1
            flights_parameters.append({
                "from": departure,
                "to": arrival,
                "passengers": passengers,
                "class": flightclass})
    return flights_parameters

def get_co2_emission_pr_flight(flights:list) -> list:
    """Gets co2 emissions from a list with dicts of flights and adds it to the dict.

    Args:
        flights (list): list with dicts of each flight

    Returns:
        list: list  of dicts with flights and its respective co2 emission.
    """
    emission_parameters = create_list_with_flights(flights)         # Creates a list of flights to the API request.
    emissions = get_flights_emission_estimate(emission_parameters)  # Gets all co2 emissions for each flight and class.

    emissions_to_final = []                                         # Collects co2e emissions for each flight.
    for emission in emissions["legs"]:
        emissions_to_final.append(emission["co2e"])

    for count, flight in enumerate(emission_parameters):            # Adds key(co2e) with its respective value to the emission_parameters list.
        flight["co2e"] = emissions_to_final[count]

    return emission_parameters


def add_emissions_to_flight(flights:list) -> list:
    """Adds the co2 emission for 'uknown', 'economic', business' and 'first' class, to each flight.

    Args:
        flights (list): list with dicts of each flight

    Returns:
        list: list of dicts with flights and its respective co2 emissions pr class
    """
    flight_emissions = get_co2_emission_pr_flight(flights)          # Gets emissions for each flight and class.
    co2index = 0
    for i, flight in enumerate(flights):                            # Adds classes ("economic", "business" etc.) to the flights
        for j in range(0,4):
            flight[flight_emissions[co2index]["class"]] = flight_emissions[co2index]["co2e"]
            co2index += 1
    return flights




