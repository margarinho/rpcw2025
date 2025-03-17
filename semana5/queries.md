1- Lista os nomes dos desportos contemplados na DBpedia: lista a sua designação e a sua descrição em inglês;
```
select distinct ?desport  ?name ?abs  where{
?desport a dbo:Sport .
?desport dbo:abstract ?abs .
FILTER ( lang(?abs) = "en") . 
?desport rdfs:label  ?name .
FILTER ( lang(?name) = "en") . 
}Limit 100

```

2- Lista os nomes e respectiva informação( nome, data nascimento, local de nascimento) dos jogadores de Polo Aquatico que estão classificiados como "Person" na Ontologia "schema.org".
```
select distinct ?atleta where{
?atleta a schema:Person  .
?atleta dbp:sport <http://dbpedia.org/resource/Water_polo> .
}

```

3- Refina a query anterior para ir buscar valores em lugar de IRIs: birthPlace...
```
select distinct  ?name ?desport  ?ori where{
?atleta a schema:Person  .
?atleta dbp:sport ?desport .
?atleta dbp:name ?name .
?atleta dbp:nationality ?ori .
}
```


4- Da lista de desportos obtida, selecionados cerca de 50.
```
```

5- Para os 50 desportos selecionados constrói um serviço em Ptyhon que vai buscar os atletas de cada um dos desportos e constrói um dataset em JSON com duas coleções: desportos e atletas.
```
```