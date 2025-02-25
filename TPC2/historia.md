# TPC2
Exercicio em _SPARQL_ sobre o dataset Historia de Portugal.

**Pergunta A:**
Quantos triplos existem na Ontologia?

**Resposta:**  51 triplos diferentes.
``` sparql
select distinct ?p where { ?s ?p ?o }
```

**Pergunta B:**
Que classes estão definidas?

**Resposta:**  42 classes diferentes.
```sparql
select distinct ?class where { 
  ?s a ?class 
}
```

**Pergunta C:**
Que propriedades tem a classe "Rei"?

**Resposta:**  16 propriedades diferentes.
```sparql
select distinct ?property where { 
  ?indiv a historia:Rei ; ?property ?value .
}
```

**Pergunta D:**
Quantos reis aparecem na ontologia?

**Resposta:**  32 Reis distintos.
```sparql
select distinct ?indiv where {
  ?indiv a historia:Rei .
}
```

**Pergunta E:**
Tabela com o seu nome, data de nascimento e cognome.
```sparql
select ?rei ?nome ?nascimento ?cognome where { 
  ?rei a historia:Rei ;
       historia:nome ?nome ;
       historia:nascimento ?nascimento ;
       historia:cognomes ?cognome .
}
``` 

**Pergunta F:** (Feito em Aula)
Acrescenta a dinastia do rei à tabela anterior.

```sparql
select ?rei ?nome ?nascimento ?cognome ?dinastia where { 
  ?rei a historia:Rei ;
       historia:nome ?nome ;
       historia:nascimento ?nascimento ;
       historia:cognomes ?cognome .
  ?reinado historia:temMonarca ?s ;
          historia:dinastia ?di .
  ?di historia:nome ? dinastia

}
```

**Pergunta G:** (Feito em Aula)
Qual a distribuição de reis pelas 4 dinastias?
```sparql
select ?dinastia (count (?monarca) as ?nmonarca) where{
  ?monarca historia:Rei .
  ?reinado historia:temMonarca ?monarca;
            historia:dinastia ?dinastia.
} group by ?dinastia
```
ou
```sparql
select ?dinastia (count (?monarca) as ?nmonarca) where{
  ?monarca historia:Rei .
  ?monarca historia:temReinado/:dinastia/:nome ?dinastia .
} group by ?dinastia
```
**Pergunta H:** (Finalizada em Aula)
Lista os descobrimentos (sua descrição) por ordem cronológica.
```sparql
select ?descobrimento ?descricao where {
  ?descobrimento a historia:Descobrimento .
  ?descobrimento a historia:Descobrimento ?descricao.
  ?descobrimento historia:data ?data .
}
order by ?data
```


**Pergunta I:**
Lista as váris conquistas, nome e data, juntamente com o nome que reinava no momento.
```sparql
select ?conquistaNome ?data ?reiNome where { 
  ?conquista a historia:Conquista ;
             historia:nome ?conquistaNome ;
             historia:data ?data ;
             historia:temReinado ?reinado .
    
  ?reinado historia:temMonarca ?rei .

  ?rei historia:nome ?reiNome .
}
```
**Pergunta:** (Feita em Aula)
Calcula a tabela com o nome, data de nascimento e numero de mandatos de todos os presidents portugueses.
```sparql
select ?nome ?data (count(?mandato) as ? nmandato) where{
    ?p a historia:Presidente ;
        historia: nome ? nome ;
        historia:nascimento ?data ; 
        historia:mandato ?mandato .
}group by ?p ?n ?data limit 100
```

**Pergunta K:**
Quantos mandamentos teve o presidente Sidónio Pais? Em que datas iniciaram e ternimaram esses mandatos?

**Resposta:**  2 mandatos distintos.
```sparql
select ?mandato ?dataInicio ?dataFim where { 
  ?mandato a historia:Mandato ;
    	   historia:chefeDeEstado ?presidente ;
           historia:comeco ?dataInicio ;
           historia:fim ?dataFim .
  ?presidente historia:nome "Sidónio Bernardino Cardoso da Silva Pais" .
}
order by ?dataInicio
```

**Pergunta L:** 
Quais os nomes dos partidos politicos presentes na ontologia?

**Resposta:**  Independente, União Nacional, Nacional Republicano, Democrático, Republicano, Socialista, Evolucionista, Liberal, Nacionalista, Social Democrata.
```sparql
seçct ?partido ?nome where { 
  ?partido a historia:Partido ;
           historia:nome ?nome .
}
```

**Pergunta M:** (Feita na Aula)
Distribuição dos militantes por partido.

```sparql
select ?nome (count(?militante) as ?nmilitante) where {
    ?partido a :Partido;
    : nome ?nome;
    :temMilitante ?militante .
}group by ?partido ?nome
```


**Pergunta N:** (Por fazer still)
Qual o partido com maior número de presidentes militantes? 

```sparql
select ?nome (count(?militante) as ?nmilitante) where {
    ?partido a :Partido;
    : nome ?nome;
    :temMilitante ?militante .
}group by ?partido ?nome
```