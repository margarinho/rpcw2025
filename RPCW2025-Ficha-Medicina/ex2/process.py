import pandas as pd
df = pd.read_csv('Disease_Syntoms')

sintomas_unicos = set()
dicionario_doencas_sintomas = {}

for index, row in df.iterrows():
    doenca = row['Disease']
    sintomas = row[1:].dropna().tolist()
    sintomas_unicos.update(sintomas)
    dicionario_doencas_sintomas[doenca] = sintomas

doenças = ''
sintomas = ''
associacao = ''

for d in dicionario_doencas_sintomas.keys():
    fd = f":{d} a :Disease ."
    doenças.append(fd)

    sintomas_associados = []
    for symptom in dicionario_doencas_sintomas[d]:
        sintomas_associados.append(f":{symptom} a :Symptom .")
        associacao.append(f":hasSymptom :{symptom}")
    
    sintomas_formatados = ', '.join(sintomas_associados)
    associacao.append(f":{d} a :Disease ; {sintomas_formatados} .")


        
        
    

    

