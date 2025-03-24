import json

with open("filmes.json", "r", encoding="utf-8") as file:
    filmes_data = json.load(file)

with open("pessoas.json", "r", encoding="utf-8") as file:
    pessoas_data = json.load(file)


rdf_output = ""

for pessoa in pessoas_data:
    id = pessoa['nconst']
    name = pessoa['primaryName']
    rdf_output += f"""
###  http://www.semanticweb.org/magui/ontologies/2025/cinem#{id}
:{id} rdf:type owl:NamedIndividual ,
                        :Pessoa ;
               :name "{name.replace(" ", "_")}" ;
               :temCategoria :{pessoa['category']} .
"""

paises = set()
for filme in filmes_data:
    if filme["region"]:
        paises.add(filme["region"])

for id in paises:
    rdf_output += f"""
###  http://www.semanticweb.org/magui/ontologies/2025/cinem#{id}
:{id} rdf:type owl:NamedIndividual ,
                         :Pais .
"""

linguas = set()
for filme in filmes_data:
    if filme["language"]:
        linguas.add(filme["language"])

for id in linguas:
    rdf_output += f"""
### http://www.semanticweb.org/magui/ontologies/2025/cinem#{id}
:{id} rdf:type owl:NamedIndividual ,
                  :Lingua .
"""

generos = set()
for filme in filmes_data:
    generos.update(filme["genres"].split(','))  # Separar géneros concatenados

for id in generos:
    rdf_output += f"""
###  http://www.semanticweb.org/magui/ontologies/2025/cinem#{id.replace(" ", "_")}
:{id.replace(" ", "_")} rdf:type owl:NamedIndividual ,
                   :Genero .
"""

for filme in filmes_data:
    id = filme['tconst']
    genres = ', '.join(f':{g.replace(" ", "_")}' for g in filme["genres"].split(','))
    originalLanguage = filme.get('language', '')
    og = f':temLingua :{originalLanguage};' if originalLanguage else ''

    rdf_output += f"""
###  http://www.semanticweb.org/magui/ontologies/2025/cinem#{id}
:{id} rdf:type owl:NamedIndividual ,
                   :Filme ;
          :temArgumento :Argumento{id} ;
          :temGenero {genres} ;
          {og}
          :temPaisOrigem :{filme["region"]} ;
          :data "{filme["startYear"]}" ;
          :duracao {filme["runtimeMinutes"]} .
"""

with open("cinema.ttl", "r", encoding="utf-8") as file:
    cinema_content = file.read()

# Concatenar o conteúdo do cinema.ttl com o rdf_output
final_output = cinema_content + "\n" + rdf_output

# Guardar no ficheiro output.ttl
with open("output.ttl", "w", encoding="utf-8") as file:
    file.write(final_output)

print("RDF atualizado e guardado em output.ttl com sucesso!")