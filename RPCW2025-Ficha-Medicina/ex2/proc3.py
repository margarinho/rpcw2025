import json
file_json = "doentes.json"

with open(file_json, 'r', encoding='utf-8') as jsonfile:
    dados = json.load(jsonfile)

string_doentes = []
for i, d in enumerate(dados):
    values = [f':{v.title().strip()}' for v in d["sintomas"]]
    s = ', '.join(values)
    string_doentes.append( f""":Patient{i+1} a :Patient ;
        :name "{d['nome']}"
        :exhibitsSymptom {s} .""")

with open('med_tratamentos.ttl', 'r') as f:
    conteudo_original = f.read()
    
with open('med_doentes.ttl', 'w', encoding='utf-8') as f:
    f.write(conteudo_original)
    f.write('\n\n')
    f.write('\n'.join(string_doentes) +'\n')