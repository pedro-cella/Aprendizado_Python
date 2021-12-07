print("====== DESAFIO 94 ======")
print("""Sobre o programa: Crie um programa que leia nome, sexo e idade de varias pessoas,
guardando os ados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A media de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da media.""")
escolha = 'S'
dicionario = {}
lista = []
while escolha != 'N':
    nome = input("Nome: ")
    dicionario['nome'] = nome
    sexo = input("Sexo [M/F]: ").upper()
    dicionario['sexo'] = sexo
    idade = int(input("Idade: "))
    dicionario['idade'] = idade
    lista.append(dicionario.copy())
    escolha = input("Quer continuar? [S/N] ").upper()
soma = 0
for k, v in enumerate(lista):
    soma += v['idade']
media = soma/len(lista)
print("-="*30)
print(f"- O grupo tem {len(lista)} pessoas.")
print(f"- A media de idade e de {media} anos.")
print(f"- As mulheres cadastradas foram: ", end='')
for k, v in enumerate(lista):
    if v['sexo'] == 'F':
        print(f"{v['nome']}", end=' ')
print()
print("Lista de pessoas que estao acima da media:")
for k, v in enumerate(lista):
    if v['idade'] >= media:
        print(f"\nnome = {v['nome']}; sexo = {v['sexo']}; idade = {v['idade']}", end='\n')
print("<< ENCERRADO >>")