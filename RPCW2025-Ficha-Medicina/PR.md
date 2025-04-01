Familia 1
Sr.João, Sra.Maria, Ana, Pedro, Rex(Cão)

Familia 2
Sr.Carlos

Pessoa
    Sr.João| Sra.Maria | Ana | Pedro | Rex(Cão)
    Sr.Carlos

Ocupações:
    Produção de Geleia |
    Agricultura | Pecuaria
    Ajudante

Pessoa > tem > Ocupação
Pessoa > ajuda > Pessoa

Contrato:
    Contrato

Pessoa > cria > Contrato
Pessoa > assina > Contrato

Proposito:
    Proteção
    Automatizar

Utilitario > tem_proposito > Propositos

Utilitario:
    Trator (nome: trator)
    Cão (nome:Rex)

Produtos
    Animais:
    Vacas, Galinhas, Porcos

    Legumes:
    tomates | alfaces | cenouras

    Frutos:
    maçãs | laranjas | bananas

    Geleias:
    maçãs | laranjas


Ajudante:


Bem
    Fazenda(localização: vila de S.José, dimenção: pequena/grande )


Posses
Pessoa > possui > Bem
Pessoa > possui > Utilitario
Pessoa > mora >  Bem

ex:
    Sr.João > possui > Fazenda
    Sr.João > produz > Animais
    Sr.João > produz > Frutas
    Sra.Maria > produz > Geleia
    Sr.Carlos > possui > Fazenda
    Sr.Carlos > possui > AnimaisDomesticos 
    Sr.João > possui > Trator

Feira:
    Feira(dia : sabados)

Vendas:
Pessoa > vende > Produto
Pessoa > participa > Feira

ex:
    Sr.João > vende > fruta
    Sr.João > vende > geleias
    Sr.Carlos > vende > legumes
    Sr.João > participa > feira
    Sr.Carlos > participa > feira

TrocasIndiretas:
Pessoa > troca_com > Pessoa

ex:
    Sr.Carlos > trocaCom > Sr.João

Trocas:
Pessoa > troca > Produto

ex:
    Sr.João > troca > fruta
    Sr.Carlos > troca > legumes

Relaçoes:
Pessoa > é casado > Pessoa
Pessoa > é_visinho > Pessoa
Pessoa > é_progenitor > Pessoa
Pessoa > é_filho > Pessoa

ex:
    Sr.João > é_casado > Sra.Maria
    Sr.Carlos > é_visinho > Sr.João
    Sr.João > é_progenitor / é_herdeiro  > Ana
    Sr.João > é_progenitor / é_herdeiro > Pedro
    Sra.Maria > é_progenitor / é_herdeiro  > Ana
    Sra.Maria > é_progenitor / é_herdeiro  > Pedro


