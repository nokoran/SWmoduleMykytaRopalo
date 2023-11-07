from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON

g = Graph()
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
SELECT ?actor1 ?actor2 ?film
WHERE {
  ?actor1 a <http://dbpedia.org/ontology/Actor> .
  ?actor2 a <http://dbpedia.org/ontology/Actor> .
  ?film <http://dbpedia.org/ontology/starring> ?actor1, ?actor2 .
  FILTER (?actor1 != ?actor2)
  ?actor1 <http://dbpedia.org/ontology/spouse> ?actor2 .
}
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# Create a set to store processed pairs
processed_pairs = set()

# Обробка та виведення результатів
for result in results["results"]["bindings"]:
    actor1_uri = result["actor1"]["value"]
    actor2_uri = result["actor2"]["value"]
    film_uri = result["film"]["value"]

    # Check if the reverse pair (actor2, actor1) is in the set
    reverse_pair = (actor2_uri, actor1_uri, film_uri)
    if reverse_pair not in processed_pairs:
        processed_pairs.add((actor1_uri, actor2_uri, film_uri))
        print(f"Сімейна акторська пара: {actor1_uri} та {actor2_uri} (фільм: {film_uri})")
