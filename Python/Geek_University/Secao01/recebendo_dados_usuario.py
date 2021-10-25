"""
Recebendo dados do usuario

input() -> Tdo dado recebido via input e do tipo String

Tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
#- Aspas dupls triplas -> """Angelina Jolie"""

# entrada de dados
# print("Qual seu nome?")
# nome = input() # Input -> Entrada

nome = input('Qual o seu nome? ')

# Exemplo de print 'antigo' 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade: ")
# idade = input()

idade = int(input('Qual sua idade?'))

# Processamento

# Saida de dados
# Exemplo de print 'antigo' 2.x
# print("O/A %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos')

"""
# int(idade) -> cast
Cast e a 'conversao' de um tipo de dado para outro.
"""
print(f'A {nome} nasceu em {2018 - idade}')
