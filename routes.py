from neo4j import GraphDatabase
import pandas as pd

uri = "bolt://3.238.38.195:7687"
password='eye-radius-platforms'
driver = GraphDatabase.driver(uri, auth=("neo4j", password))

df = pd.read_csv('routes.csv')
print(df)
print(df.columns)

def add_routes(tx, airline, airline_id, source_airport, source_airport_id, destination_airport, destination_airport_id, codeshare, stops, equipment):
    tx.run(
        "CREATE (:Routes{airline: $airline, airline_id: $airline_id, source_airport: $source_airport, "
        "source_airport_id: $source_airport_id, "
        "destination_airport: $destination_airport, destination_airport_id: $destination_airport_id, "
        "codeshare: $codeshare, stops: $stops, equipment: $equipment})",
        airline=airline, airline_id=airline_id, source_airport=source_airport, source_airport_id=source_airport_id, destination_airport=destination_airport, destination_airport_id= destination_airport_id, codeshare=codeshare, stops=stops, equipment=equipment)


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

with driver.session() as session:
    for _, row in df.iterrows():
        session.execute_write(add_routes,
                              row.iloc[0],  # Airline
                              convert_to_int(row.iloc[1]), # Airline_ID
                              row.iloc[2],  # Source_Airport
                              convert_to_int(row.iloc[3]),  # Source_Airport_ID
                              row.iloc[4],  # Destination_airport
                              convert_to_int(row.iloc[5]),  # Destination_airport_ID
                              row.iloc[6],  # Codeshare
                              convert_to_int(row.iloc[7]), # Stops
                              row.iloc[8])  # Equipment


