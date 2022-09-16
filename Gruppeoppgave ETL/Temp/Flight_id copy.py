import json

def flight_id(flightdata:dict) -> dict:
    """Takes in a json file and returns a dict with index, flight_id, 
    departure from airport and arrival at airport.

    Args:
        flightdata (dict): json path from Avinor

    Returns:
        list: dicts with flights example: [{"flight_id": A3757, "airport_dep": "OSL", "airport_arr": "ATH"}]
    """
    with open(flightdata, "r") as fp:
        flightdata = json.load(fp)
        flights = flightdata["airport"]["flights"]["flight"]
        
        flight_id_airport = []

        for flight in flights:
            flight_id = flight["flight_id"]

            if flight["arr_dep"] == "D":
                airport_arr = flight["airport"]
                airport_dep = "OSL"
                flight_id_airport.append({
                                        "flight_id": flight_id, 
                                        "airport_dep": airport_dep,
                                        "airport_arr": airport_arr
                                        })
            elif flight["arr_dep"] == "A":
                airport_arr = "OSL"
                airport_dep = flight["airport"]
                flight_id_airport.append ({
                                        "flight_id": flight_id, 
                                        "airport_dep": airport_dep,
                                        "airport_arr": airport_arr
                                        })
            else:
                return "missing value in flight['arr_dep']"

        return flight_id_airport
        