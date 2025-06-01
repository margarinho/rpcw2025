import pandas as pd
import json

df = pd.read_csv('Disease_Syntoms')
dt = pd.read_csv('Disease_Treatment')
dd = pd.read_csv('Disease_Treatment')

with open('doentes.json') as f:
    doentes = json.load(f)

doentes_ttl = ""
for i, d in enumerate(doentes):
    
    linha = f':Patient{i} a :Patient ; \n  :name "{d['name']}'
    sintomas_ls = ""
    for s in d['sintomas']:
        sintomas_ls.append(f":exhibitsSymptom :{s}")
        
    sintomas_ls_formatados = ';\n '.join(sintomas_ls)
    doentes_ttl.append(f':Patient{i} a :Patient ; \n  :name "{d['name']}\n {sintomas_ls_formatados} .\n')


sintomas_unicos = set()
tratamentos_unicos = set()

dicionario_doencas_sintomas = {}
dicionario_doencas_tratamentos = {}

for index, row in df.iterrows():
    doenca = row['Disease']
    sintomas = row[1:].dropna().tolist()
    sintomas_unicos.update(sintomas)
    dicionario_doencas_sintomas[doenca] = sintomas
    
for index, row in dt.iterrows():
    doenca = row['Disease']
    tratamentos = row[1:].dropna().tolist()
    tratamentos_unicos.update(tratamentos)
    dicionario_doencas_tratamentos[doenca] = tratamentos
    
    

doencas = ''
sintomas = ''
associacao = ''
tratamento = ''

for d in dicionario_doencas_sintomas.keys():
    fd = f":{d} a :Disease .\n"
    doencas.append(fd)

    sintomas_associados = []
    for symptom in dicionario_doencas_sintomas[d]:
        sintomas_associados.append(f":{symptom} a :Symptom .\n")
        associacao.append(f":{symptom}")

    tratamentos_associados = []
    for tratamento in dicionario_doencas_tratamentos[d]:
        tratamentos_associados .append(f":{tratamento} a :Treatment .\n")
        associacao.append(f":hasTreatment :{symptom}")
        
    
    sintomas_formatados = ', '.join(sintomas_associados)
    associacao.append(f":{d} a :Disease ; :hasSymptom {sintomas_formatados} ;\n")

    tratamentos_formatados = ', '.join(tratamentos_associados)
    associacao.append(f":hasTreatment {tratamentos_formatados} .\n")

inicio = """
@prefix : <http://www.example.org/disease-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix swrl: <http://www.w3.org/2003/11/swrl#> .
@prefix swrlb: <http://www.w3.org/2003/11/swrlb#> .

<http://www.example.org/disease-ontology> rdf:type owl:Ontology .\n"""

linhas =[inicio,doencas,sintomas,associacao, doentes_ttl]

with open("ex2/med_doentes.ttl", "w") as arquivo:
    arquivo.writelines(linhas)
    



    

