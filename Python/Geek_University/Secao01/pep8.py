"""
PEP8 - Python Enhancement Proposal
Sao propostas de melhorias para a linguagem Python
Zem of Python
import this

A ideia da PEP8 e que possamos escrever codigos Python de forma Pythonica.
[1] - Utilize Camel Case para nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica
    pass


[2] - Utilize nomes em minusculo, separados por underline para funcoes ou variaveis;
def soma():
    pass

def soma_dois();
    pass


numero = 4
numero_impar = 5


[3] - Utilize 4 espacos para a identacao! (NAO use TAB)
if 'a' in 'banana':
    print('tem')


[4] - Linhas em branco
- Separar funcoes e definicoes de classe com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco
class Classe:
    pass


class Outra:
    pass


[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;


# Import Errado

import sys, os

# Import Certo

import sys
import os

Nao ha problemas em utilizar"

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings e 
# antes de constantes ou variaveis globais

[6] - Espacos em expressoes e instrucoes

# Nao faca:

funcao( algo[ 1 ], { outro: 2 } )

# Faca:

funcao(algo[1] {outro: 2})

# Nao faca:

algo (1)

# Faca

algo(1)

# Nao faca:

dict ['chave'] = list [indice]

# Faca:

dict['chave' = lista[indice]

# Nao faca:

x              = 1
y              = 3
variavel_longa = 5

# Faca

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrucao com uma nova linha
"""
import this
