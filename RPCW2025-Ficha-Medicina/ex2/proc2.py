import csv
file_csv = "Disease_Treatment.csv"

rows_1 = []
fields_1 = []

with open(file_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields_1 = next(csvreader)
    
    for row in csvreader:
        rows_1.append(dict(zip(fields_1, row)))

#Disease,Precaution_1,Precaution_2,Precaution_3,Precaution_4

tratamentos = set()
doença_trata = {}
for row in rows_1:
    doença_value = set()
    disease = row['Disease']
    for s in list(row.values())[1:]:
        t = s.title().replace(' ', '_')
        tratamentos.add(t)
        doença_value.add(t)
    
    if disease in doença_trata:
        doença_trata[disease].update(doença_value)
    else:
        doença_trata[disease] = doença_value

#instancia de tratamento

string_tratamentos = []
for s in tratamentos:
    string_tratamentos.append(f":{s.title().strip()} a :Treatment .")
    
#associação
string_dt = []
for key, value in doença_trata.items():
    values = [f':{v.title().strip()}' for v in value if v]
    
    s = ', '.join(values)
    string_dt.append(f':{key.title()} :hasTreatment {s} . ')

with open('med_doencas.ttl', 'r') as f:
    conteudo_original = f.read()
    
with open('med_tratamentos.ttl', 'w', encoding='utf-8') as f:
    f.write(conteudo_original)
    f.write('\n\n')
    f.write('\n'.join(string_tratamentos) +'\n')
    f.write('\n\n')
    f.write('\n'.join(string_dt) +'\n')

