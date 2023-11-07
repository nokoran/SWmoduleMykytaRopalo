from rdflib import Graph, Namespace
graph = Graph()
graph.parse('countries_info.ttl')

"""Вивід країн та відповідних їм сусідів"""
query = """
    SELECT ?country_name ?country ?country_neighbour
    WHERE {
        ?country_neighbour :country_neighbour_value  ?country .
    }
    """

res = graph.query(query)
for row in res:
    print(f"country: {row}")



#не зміг зробити з площами