from neo4j import GraphDatabase

uri = "bolt://3.238.38.195:7687"
password = 'eye-radius-platforms'
driver = GraphDatabase.driver(uri, auth=("neo4j", password))


def propose_itineraire(departure_airport, destination_airport):
    with driver.session() as session:
        result = session.run("""
            MATCH path = (a:Airport {iata: $departure_iata})-[:DEPARTURE_FROM*]->(r:Routes)-[:ARRIVE_AT]->(b:Airport {iata: $destination_iata})
            RETURN path
            ORDER BY length(path)
            LIMIT 1
            """, departure_iata=departure_airport, destination_iata=destination_airport)

        if result.peek() is not None:
            path = result.peek()["path"]
            airport_names = [node["name"] for node in path.nodes]
            print("Itinéraire trouvé :")
            print(" -> ".join(airport_names))
        else:
            print("Aucun itinéraire trouvé entre les aéroports spécifiés.")


# Exemple d'utilisation
depart = "CDG"  # Code IATA de l'aéroport de départ
destination = "KIX"  # Code IATA de l'aéroport de destination
propose_itineraire(depart, destination)
