import psycopg2

def compare_avinor_climatiq():
    """
    [{"flight_id": "A3757", "airport_dep": "OSL", "airport_arr": "ATH"}]
    """
    conn = psycopg2.connect("dbname=d26q679v0a08m9, user=wjrnshvsyrjebr")

    flightdata = []
    
    with conn.cursor() as cur:
        cur.execute("""
                SELECT a.flight_ id, a.origin, a.destination FROM avinor a
                WHERE NOT EXISTS (
                SELECT c.flight_id FROM climatiq
                WHERE a.flight_id = c.flight_id
                )
                """)
        for row in cur:
            flightdata.append({row})

    conn.close()

    return flightdata

def write_to_qlimatic(flights_with_emissions):
    conn = psycopg2.connect("dbname=test, user=postgres")    
    with conn.cursor() as cur:
        for row in flights_with_emissions:
            cur.execute("""
                    INSERT INTO qlimatic (flight_id, airport_dep, airport_arr, uknown, economy, business, first)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""", [row[0], row[1], row[2], row[3], row[4], row[5], row[6]])


