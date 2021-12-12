from utilidadesCeV import dado
from utilidadesCeV import moeda

print("====== DESAFIO 112 ======")
print("""Sobre o programa: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um modulo chamado dado.
Crie uma funcao chamada leiaDinheiro() que seja capaz de funcionar input(), mas com uma validacao de dados
para aceitar apenas valores que sejam monetarios.""")

p = dado.leiaDinheiro("Digite um preco: R$")
moeda.resumo(p, 35, 22)