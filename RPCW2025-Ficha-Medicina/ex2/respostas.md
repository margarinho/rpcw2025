1. Quantas doenças estão presentes na ontologia? 
```
select (Count(?doencas) ?ndoencas)
where{
    ?doenca a :Disease .
}
```
2. Que doenças estão associadas ao sintoma "yellowish_skin"?
```
select (Count(?doencas) ?ndoencas)
where{
    ?doenca a :Disease ;
    :hasSymptom :Yellowish_Skin .
}
```
3. Que doenças estão associadas ao tratamento "exercise"?
```
select (Count(?doencas) ?ndoencas)
where{
    ?doenca a :Disease ;
    :hasTreatment :Exercise .
}
```
4. Produz uma lista ordenada alfabeticamente com o nome dos doentes.
```
select ?nome
where{
    ?doente a :Patient ;
    :name ?nome .
}
order by ASC(?nome)
```
5.  Triplos com a forma :patientX :hasDisease :diseaseY.
```
Construct
{
     :patient :hasDisease :disease
}
where{
    ?patient a :Patient ;
    :hasSymptom ?s.
    ?diease a :Disease;
    :hasSymptom ?s.
}
```
6. (doença, nº de doentes)
```
select doenca (Count(?patient) ?npatient)
where{
    ?doenca a :Disease ;
    :hasSymptom ?s .
    ?patient a :Patient ;
    :hasSymptom ?s .
}
Group by (?doenca)
Order by DESC(?npatient)
```
7. (sintoma, nº de doenças com o sintoma)
```
select sintoma (Count(?patient) ?npatient)
where{
    ?patient a :Patient ;
    :hasSymptom ?sintoma .
}
Group by (?sintoma)
Order by DESC(?npatient)
```
8. (tratamento, nº de doenças com o tratamento)
```
select trata (Count(?doenca) ?ndoenca)
where{
    ?doenca a :Disease ;
    :hasTreatment ?trata .
    ?patient a :Patient ;
    :hasSymptom ?s .
}
Group by (?trata)
Order by DESC(?ndoenca)
```