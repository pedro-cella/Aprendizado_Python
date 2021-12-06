print("====== DESAFIO 84 ======")
print("""Sobre o programa: Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. 
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.""")
escolha = 'S'
lista = list()
pessoa = list()
maior = 0
menor = 1000
pesadas = list()
leves = list()
while escolha != 'N':
    pessoa.append(input("Nome: "))
    pessoa.append(float(input("Peso: ")))
    lista.append(pessoa[:])
    pessoa.clear()
    escolha = input("Quer continuar? [S/N] ").upper()
print("-="*30)
print(f"Ao todo voce cadastrou {len(lista)} pessoas")
for peso in lista:
    if peso[1] > maior:
        maior = peso[1]
    if peso[1] < menor:
        menor = peso[1]
print(f"O maior peso foi o de {maior}Kg. Peso de ", end='')
for p in lista:
    if p[1] == maior:
        print(f"[{p[0]}]", end='')
print()
print(f"O menor peso foi o de {menor}Kg. Peso de ", end='')
for p in lista:
    if p[1] == menor:
        print(f"[{p[0]}]", end='')
print()
    