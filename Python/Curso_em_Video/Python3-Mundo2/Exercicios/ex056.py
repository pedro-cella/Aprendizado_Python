print("====== DESAFIO 56 ======")
print("""Sobre o programa: Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- A media de idade do grupo;
- Qual o nome do homem mais velho;
- Quantas mulheres tem menos de 20 anos.""")
soma_idade = 0
soma_mulheres = 0
mais_velho = 0
nome_mais_velho = 'a'
for i in range(1, 5):
    print("Pessoa {}".format(i))
    nome = input("Insira seu nome: ")
    idade = int(input("Insira sua idade: "))
    sexo = input("Insira seu sexo(M ou F): ").upper()
    print("\n")
    soma_idade += idade
    if sexo == 'M' and idade > mais_velho:
        nome_mais_velho = nome
        mais_velho = idade
    elif sexo == 'F' and idade < 20:
        soma_mulheres += 1   
print("Media de idade do grupo: {}".format(soma_idade/4))
if nome_mais_velho != 'a':
    print("O homem mais velho do grupo e {} com {} anos".format(nome_mais_velho, mais_velho))
else:
    print("Nao existem homens no grupo")

if soma_mulheres >= 1:
    print("Existem {} mulhere(s) com menos que 20 no grupo".format(soma_mulheres))
else:
    print("Ou nao existem mulheres no grupo, ou as que existem nao possuem menos que 20")