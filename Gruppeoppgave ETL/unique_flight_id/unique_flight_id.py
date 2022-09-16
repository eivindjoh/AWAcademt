import json
import pandas as pd

with open("unique_flight_id/flightdata.json", "r") as fp_dep:
    flightdata_dep = json.load(fp_dep)
    
    flights_dep = flightdata_dep["airport"]["flights"]["flight"]
    
    flight_id_airport_dep = {}

    for count, flight in enumerate(flights_dep):
        flight_id_dep = flight["flight_id"]
        airport_dep = flight["airport"]
        flight_id_airport_dep[f"{count}"] = {"flight_id":flight_id_dep,"airport":airport_dep}

with open("unique_flight_id/flightdataArrival.json", "r") as fp:
    flightdata_arr = json.load(fp)
    
    flights_arr = flightdata_arr["airport"]["flights"]["flight"]
    
    flight_id_airport_arr = {}

    for count, flight in enumerate(flights_arr):
        flight_id_arr = flight["flight_id"]
        airport_arr = flight["airport"]
        flight_id_airport_arr[f"{count}"] = {"flight_id":flight_id_arr,"airport":airport_arr}

df_dep = pd.DataFrame.from_dict(flight_id_airport_dep, orient="index")
df_arr = pd.DataFrame.from_dict(flight_id_airport_arr, orient="index")

df = pd.concat([df_dep, df_arr]).sort_values("flight_id")
df.to_csv("out.csv")