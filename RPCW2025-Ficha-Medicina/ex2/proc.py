import csv

file_csv = "Disease_Description.csv"

rows_1 = []
fields_1 = []

with open(file_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields_1 = next(csvreader)
    
    for row in csvreader:
        rows_1.append(dict(zip(fields_1, row)))

file_csv_2 = "Disease_Syntoms.csv"

rows_2 = []
fields_2 = []

with open(file_csv_2, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields_2 = next(csvreader)
    
    for row in csvreader:
        rows_2.append(dict(zip(fields_2, row)))

#instancia de cada doença
doenças = []
string_doenças = []
for row in rows_1:
    string_doenças.append( f":{row['Disease']} a :Disease .")
    
#--------------------------------------
sintomas = set()
doença_sintomas = {}

for row in rows_2:
    doença_value = set()
    disease = row['Disease']
    for s in list(row.values())[1:]:
        sintomas.add(s)
        doença_value.add(s)
    
    if disease in doença_sintomas:
        doença_sintomas[disease].update(doença_value)
    else:
        doença_sintomas[disease] = doença_value

#instancia de cada sintoma
string_sintomas = []
for s in sintomas:
    string_sintomas.append(f":{s.strip()} a :Symptom .")

#Associação da doença aos sintomas
string_ds = []
for key, value in doença_sintomas.items():
    values = [f':{v.strip()}' for v in value if v]
    
    s = ', '.join(values)
    string_ds.append(f':{key} :hasSymptom {s} . ')

    
with open('medical.ttl', 'r') as f:
    conteudo_original = f.read()
    
with open('med_doencas.ttl', 'w', encoding='utf-8') as f:
    f.write(conteudo_original)
    f.write('\n\n')
    f.write('\n'.join(string_doenças) +'\n')
    f.write('\n\n')
    f.write('\n'.join(string_sintomas) +'\n')
    f.write('\n\n')
    f.write('\n'.join(string_ds) +'\n')
