import pandas as pd

df = pd.read_csv('Disease_Syntoms')


syntoms = set()

diseases_syntoms = {}

for index, row in df.iterrows():
    # cria um dicionario com {doenca: {symptom:[syntoms], treatment:[treatments]}}
    # set dos sintomas
    
    d = row['Disease']
    s = row[1:].dropna().tolist()
    syntoms.add(s)
    diseases_syntoms[d] = {"hasSymptom" : s}

def str_ind_set(struct, type):
    q = ""
    for entry in struct:
        l = f":{entry} a :{type} . \n"
        q.append(l)
    return q


def str_ind_dic(struct, type):
    ttl = []
    for c , op in struct.items():
        own_type = f":{c} a :{type} ;\n"
        properties = ''
        
        for name , values in op.items():
            properties.append(f"{name} {' ,'.join(f":{val}" for val in values)}")
            
        r = ';\n'.join(properties)
        ttl.append(own_type + r + ' .')
        
    return '\n'.join(ttl)

