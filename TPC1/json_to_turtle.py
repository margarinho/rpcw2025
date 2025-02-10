import json

def json_to_turtle(json_file, ttl_base_file, output_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    with open(ttl_base_file, "r", encoding="utf-8") as f:
        ttl_base = f.read()
        
    ttl_base_lines = ttl_base.splitlines()
    ttl_base_last_line = ttl_base_lines[-1] if ttl_base_lines else ""
    ttl_base_without_last_line = "\n".join(ttl_base_lines[:-1])
    
    atletas = []
    exames = []
    modalidades = set()
    

    
    for i, entry in enumerate(data, start=1):
        atleta_id = f"Atleta{i}"
        exame_id = f"Exame{i}"
        modalidade_id = entry["modalidade"].replace(" ", "_")
        modalidades.add((modalidade_id, entry['modalidade']))
        
        atletas.append(f"###  http://www.semanticweb.org/magui/ontologies/2025/untitled-ontology-3#{atleta_id}")
        atletas.append(f":{atleta_id} rdf:type owl:NamedIndividual , :Atleta ;")
        atletas.append(f"         :pratica :{modalidade_id} ;")
        atletas.append(f"         :atletaClube \"{entry['clube']}\" ;")
        atletas.append(f"         :atletaEmail \"{entry['email']}\" ;")
        atletas.append(f"         :atletaFederado \"{str(entry['federado']).lower()}\"^^xsd:boolean ;")
        atletas.append(f"         :atletaIdade {entry['idade']} ;")
        atletas.append(f"         :atletaMorada \"{entry['morada']}\" ;")
        atletas.append(f"         :atletaNome \"{entry['nome']['primeiro']}\" ;")
        atletas.append(f"         :atletaSobrenome \"{entry['nome']['último']}\" .\n")
        
        exames.append(f"###  http://www.semanticweb.org/magui/ontologies/2025/untitled-ontology-3#{exame_id}")
        exames.append(f":{exame_id} rdf:type owl:NamedIndividual , :Exame ;")
        exames.append(f"        :avalia :{atleta_id} ;")
        exames.append(f"        :exameData \"{entry['dataEMD']}\" ;")
        exames.append(f"        :exameId \"{entry['_id']}\" ;")
        exames.append(f"        :exameIdx {entry['index']} ;")
        exames.append(f"        :exameResultado \"{str(entry['resultado']).lower()}\"^^xsd:boolean .\n")
    
    modalidades_ttl = []
    for modalidade_id, modalidade_nome in modalidades:
        modalidades_ttl.append(f"###  http://www.semanticweb.org/magui/ontologies/2025/untitled-ontology-3#{modalidade_id}")
        modalidades_ttl.append(f":{modalidade_id} rdf:type owl:NamedIndividual , :Modalidade ;")
        modalidades_ttl.append(f"         :mobilidadeNome \"{modalidade_nome}\" .\n")
        

    titulo = "#################################################################\n#    Individuals\n#################################################################\n"
   
    final_content = ttl_base_without_last_line + "\n" + titulo + "\n" + " \n".join(atletas + exames + modalidades_ttl) + "\n" + ttl_base_last_line
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_content)

    

# Exemplo de uso:
json_to_turtle("emd.json", "base.ttl", "exames.ttl")
