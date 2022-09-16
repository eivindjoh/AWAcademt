from Flight_id import flight_id
from Co2emissions import get_flights_emission_estimate




# fra flight_id.py
flights = [{0: {"flight_id": "A377", "airport_dep": "BER", "airport_arr": "HAM"}}, {1: {"flight_id": "A3757", "airport_dep": "OSL", "airport_arr": "ATH"}}]

def create_list_with_flights(flights:list) -> list:
    """Creates a list with flights with 1 passenger for each class in that flight.

    Args:
        flights (dict): ex. [{"1": {"flight_id": "A3757", "airport_dep": "OSL", "airport_arr": "ATH"}}]

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
    for count, flight in enumerate(flights):
        values = flight[count]
        flightclasses = ["unknown", "economy", "business", "first"]
        for flightclass in flightclasses:
            departure = values["airport_dep"]
            arrival = values["airport_arr"]
            passengers = 1
            flights_parameters.append({
                "from": departure,
                "to": arrival,
                "passengers": passengers,
                "class": flightclass})
    return flights_parameters

def get_co2_emission_pr_flight(flights):
    flight_parameters = create_list_with_flights(flights)
    emissions = get_flights_emission_estimate(flight_parameters)

    emissions_to_final = []
    for emission in emissions["legs"]:
        emissions_to_final.append(emission["co2e"])

    for count, flight in enumerate(flight_parameters):
        flight["co2e"] = emissions_to_final[count]

    return flight_parameters


def add_emissions_to_flight(flights):
    flight_emissions = get_co2_emission_pr_flight(flights)
    co2index = 0
    for i, flight in enumerate(flights):
        for j in range(0,4):
            flight[i][flight_emissions[co2index]["class"]] = flight_emissions[co2index]["co2e"]
            co2index += 1
    return flights


