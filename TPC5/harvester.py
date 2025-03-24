# Harvester.py
# 24 março de 2025

import requests
import json

def executar_sparql_query(endpoint_url, sparql_query):
    headers = {'Accept': 'application/sparql-results+json'}
    params = {'query': sparql_query, 'format': 'json'}
    response = requests.get(endpoint_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados do endpoint SPARQL. Status Code: {response.status_code}")
        print(f"Resposta: {response.text}") 
        return None

def consultar_atores_por_id(atores_ids):
    atores_info = []
    for ator_id in atores_ids:
        sparql_query_two = f"""
            SELECT ?name ?birthDate ?birthPlace ?abstract WHERE {{
                <{ator_id}> rdfs:label ?name .
                <{ator_id}> dbo:birthDate ?birthDate .
                <{ator_id}> dbo:birthPlace ?birthPlace .
                <{ator_id}> dbo:abstract ?abstract .

                FILTER(lang(?name) = "en")
                FILTER(lang(?abstract) = "en")
            }}
        """

        resultado_atores = executar_sparql_query(endpoint_url, sparql_query_two)

        if resultado_atores:
            for binding in resultado_atores['results']['bindings']:
                ator = {
                    'name': binding['name']['value'],
                    'birthDate': binding['birthDate']['value'],
                    'birthPlace': binding['birthPlace']['value'],
                    'abstract': binding['abstract']['value']
                }
                atores_info.append(ator)

    return atores_info

def processar_resultados(resultado):
    filmes = []
    atores_ids = set()

    for binding in resultado['results']['bindings']:
        id_filme = binding['id']['value']
        title = binding.get('title', {}).get('value', 'N/A')
        origin = binding.get('origin', {}).get('value', 'N/A')
        producer = binding.get('producer', {}).get('value', 'N/A')
        writer = binding.get('writer', {}).get('value', 'N/A')
        abs = binding.get('abs', {}).get('value', 'N/A')
        starring = binding.get('starring', {}).get('value', 'N/A')

        if starring != 'N/A':
            atores_ids.add(starring)

        filmes.append({
            'id_filme': id_filme,
            'title': title,
            'origin': origin,
            'producer': producer,
            'writer': writer,
            'abs': abs,
            'starring': starring
        })

    atores_info = consultar_atores_por_id(list(atores_ids))

    return filmes, atores_info

endpoint_url = "https://dbpedia.org/sparql"

sparql_query_one = f"""
    SELECT DISTINCT ?id ?title ?origin ?producer ?writer ?abs ?starring WHERE {{
        ?id a schema:Movie .
        ?id dbp:name ?title .
        ?id dbp:country ?origin .
        ?id dbo:producer/dbp:name ?producer .
        ?id dbo:writer/dbp:name ?writer .
        ?id dbo:abstract ?abs .
        ?id dbo:starring ?starring .

        FILTER(lang(?title) = "en")
        FILTER(lang(?origin) = "en")
        FILTER(lang(?producer) = "en")
        FILTER(lang(?abs) = "en")
    }} 
    ORDER BY RAND() 
    LIMIT 100
"""

resultado = executar_sparql_query(endpoint_url, sparql_query_one)

if resultado:
    filmes, atores_info = processar_resultados(resultado)

    resultado_json = {
        "filmes": []
    }

    for filme in filmes:
        filme_info = {
            'id_filme': filme['id_filme'],
            'title': filme['title'],
            'origin': filme['origin'],
            'producer': filme['producer'],
            'writer': filme['writer'],
            'abs': filme['abs'],
            'starring': []
        }

        for ator in atores_info:
            filme_info['starring'].append({
                'name': ator['name'],
                'birthDate': ator['birthDate'],
                'birthPlace': ator['birthPlace'],
                'abstract': ator['abstract']
            })

        resultado_json['filmes'].append(filme_info)

    with open("resultado_filmes.json", "w", encoding="utf-8") as f:
        json.dump(resultado_json, f, ensure_ascii=False, indent=4)

    print("Resultado salvo em 'resultado_filmes.json'.")
else:
    print("Nenhum resultado encontrado.")

