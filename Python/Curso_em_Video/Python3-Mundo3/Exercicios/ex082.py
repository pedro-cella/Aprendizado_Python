print("====== DESAFIO 82 ======")
print("""Sobre o programa: Crie um programa que leia varios numeros e coloque-os em uma lista.
Depois disso, crie duas lisras extras que vao conter apenas os pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteudo das tres listas geradas.""")
escolha = 'S'
lista = []
pares = []
impares = []
while escolha != 'N':
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    escolha = input("Deseja continuar? [S/N] ").upper()
print("-="*30)
print(f"A lista completa e {lista}")
print(f"A lista de pares e {pares}")
print(f"A lista de impares e {impares}")