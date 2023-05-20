from neo4j import GraphDatabase
import pandas as pd

uri = "bolt://3.238.38.195:7687"
password='eye-radius-platforms'
driver = GraphDatabase.driver(uri, auth=("neo4j", password))

with driver.session() as session:
    result = session.run("""
        MATCH (a:Airport), (r:Routes)
        WHERE a.iata = r.source_airport
        MERGE (a)-[:DEPARTURE_FROM]->(r)
    """)

with driver.session() as session:
    result = session.run("""
        MATCH (a:Airport), (r:Routes)
        WHERE a.iata = r.source_airport
        MERGE (r)-[:ARRIVE_AT]->(a)
        RETURN r.destination_airport
    """)
    for record in result:
        print(record["r.destination_airport"])
