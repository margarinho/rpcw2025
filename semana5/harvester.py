# Harvester.py
# 11 março de 2025

import json
from query import query_graphdb

with open("desport.json") as f:
    desports = json.load(f)

dataset = [{}]
endpoint = "https://dbpedia.org/sparql"

for d in desports:
    sparql_query_d = f"""
        select distinct ?name ?abs  where{{
            <{d}> dbo:abstract ?abs .
            <{d}> rdfs:label ?name .
            FILTER ( lang(?abs) = "en") .
            FILTER ( lang(?name) = "en") . 
            }}
    """
    
    result_d = query_graphdb(endpoint, sparql_query_d)
    


    sparql_query_a = f"""
            select distinct ?atleta ?name ?ori ?data where{{
                ?atleta a schema:Person  .
                ?atleta dbp:sport <{d}> .
                ?atleta dbp:name ?name .
                ?atleta dbp:nationality ?ori .
                ?atleta dbp:birthDate ?data .
            }}
    """
    result_a = query_graphdb(endpoint, sparql_query_a)
    
    atletas = []
    for a in result_a['results']['bindings']:
        atletas.append({
            "id": a['atleta']['value'],
            "nome": a['name']['value'],
            "origem": a['ori']['value'],
            "dataNasc": a['data']['value']
        })
    
    dataset.append(
        {
            "id": d,
            "designacao": result_d['results']['bindings'][0]['name']['value'],
            "abs": result_d['results']['bindings'][0]['abs']['value'],
            "atletas": atletas
        }
    )

        
with open("dataset.json", 'w') as fout:
    json.dump(dataset, fout, ensure_ascii=False)
        