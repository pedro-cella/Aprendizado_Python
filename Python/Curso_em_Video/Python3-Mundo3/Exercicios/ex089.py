print("====== DESAFIO 89 ======")
print("""Sobre o programa: Crie um programa que leia nome e duas notas de varios alunos
e guarde tudo em uma lista comoposta. No final, mostre um boletim contendo a media
de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.""")
escolha = 'S'
lista = []
aluno = []
while escolha != 'N':
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media])
    escolha = input("Quer continuar? [S/N] ").upper()
print("-="*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print("-"*26)
for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-"*35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f"Notas de {lista[opc][0]} sao {lista[opc][1]}")
print("<<< VOLTE SEMPRE >>>")