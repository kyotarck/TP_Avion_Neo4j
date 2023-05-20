from neo4j import GraphDatabase
import pandas as pd

uri = "bolt://3.238.38.195:7687"
password='eye-radius-platforms'
driver = GraphDatabase.driver(uri, auth=("neo4j", password))

df = pd.read_csv('airports.csv')
print(df)
print(df.columns)

def add_airport(tx, id, name, city, country, iata, icao, latitude, longitude, altitude, timezone, dst, tz_database_time_zone, type, source):
    tx.run(
        "CREATE (:Airport {id: $id, name: $name, city: $city, country: $country, iata: $iata, icao: $icao, latitude: $latitude, longitude: $longitude, altitude: $altitude, timezone: $timezone, dst: $dst, tz_database_time_zone: $tz_database_time_zone, type: $type, source: $source})",
        id=id, name=name, city=city, country=country, iata=iata, icao=icao, latitude=latitude, longitude=longitude,
        altitude=altitude, timezone=timezone, dst=dst, tz_database_time_zone=tz_database_time_zone, type=type,
        source=source)

with driver.session() as session:
    for _, row in df.iterrows():
        session.execute_write(add_airport,
                              int(row.iloc[0]),# Airport_ID
                              row.iloc[1],  # Name
                              row.iloc[2],  # City
                              row.iloc[3],  # Country
                              row.iloc[4],  # IATA
                              row.iloc[5],  # ICAO
                              float(row.iloc[6]),  # Latitude
                              float(row.iloc[7]), # Longitude
                              int(row.iloc[8]),  # Altitude
                              row.iloc[9],  # Timezone
                              row.iloc[10],  # DST
                              row.iloc[11],  # Tz_database_time_zone
                              row.iloc[12],  # Type
                              row.iloc[13])  # Source


