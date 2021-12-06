print("====== DESAFIO 81 ======")
print("""Sobre o programa: Crie um programa que leia varios numeros e coloque-os em uma lista.
Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou nao na lista.""")
lista = []
numero = int(input("Digite um valor: "))
lista.append(numero)
escolha = input("Deseja continuar? [S/N] ").upper()
while escolha != 'N':
    numero = int(input("Digite um valor: "))
    lista.append(numero)
    escolha = input("Deseja continuar? [S/N] ").upper()
lista.sort(reverse = True)
print("-="*30)
print(f"Voce digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente sao {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 nao foi encontrado na lista!")