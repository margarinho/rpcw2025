# Harvester.py
# 11 março de 2025

import json
from query_graphdb import query_graphdb

endpoint = "https://dbpedia.org/sparql"

sparql_query_one = f"""
    select distinct ?id ?title ?origin ?producer ?writer ?abs where {{
    ?id a schema:Movie .

    ?id dbp:name ?title .
    ?id dbp:country ?origin .
    ?id dbo:producer/dbp:name ?producer .
    ?id dbo:writer/dbp:name ?writer .
    ?id dbo:abstract ?abs .
    
    filter(lang(?title)="en")
    filter(lang(?origin)="en")
    filter(lang(?producer)="en")
    filter(lang(?abs)="en")
    
}} ORDER BY RAND() LIMIT 100
    """
    
result_movies = query_graphdb(endpoint, sparql_query_one)

dataset = {"movies" : [],
           "actors" : []
           }

for m in result_movies['results']['bindings']:
    
    starring = query_graphdb(endpoint, f'''
    select ?starring where {{
        <{m['id']['value']}> dbo:starring ?starring .
    }} LIMIT 4
    ''')
    
    starring_actors = [s['starring']['value'] for s in starring['results']['bindings']]
    
    dataset['movies'].append({
            "Id": m['id']['value'],
            "Title": m['title']['value'],
            "Country": m['origin']['value'],
            "Producer": m['producer']['value'],
            "Argument": m['writer']['value'],
            "Abstract": m['abs']['value'],
            "Starring": starring_actors
        })
    
    for a in starring_actors:
        print(a)
        
        sparql_query_two = f"""
            select distinct ?name ?birth ?origin ?abs where{{
                    <{a}> foaf:name ?name .
                    <{a}> dbo:birthDate ?birth .
                    <{a}> dbo:birthPlace ?origin .
                    <{a}> dbo:abstract ?abs .
                }}
        """
        
        result_actor = query_graphdb(endpoint, sparql_query_two)
        
        if result_actor['results']['bindings']:
            actor = result_actor['results']['bindings'][0]
            dataset['actors'].append({
                "Name": actor['name']['value'],
                "Birth": actor['birth']['value'],
                "Origin": actor['origin']['value'],
                "Abstract": actor['abs']['value']
            })
    
      
      
with open("movies_dataset.json", 'w') as fout:
    json.dump(dataset, fout, ensure_ascii=False)
        
