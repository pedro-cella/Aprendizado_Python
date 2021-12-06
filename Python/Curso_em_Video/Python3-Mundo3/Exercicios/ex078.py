print("====== DESAFIO 78 ======")
print("""Sobre o programa: Faca um programa que leia 5 valores numericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista.""")
numeros = []
for posicao, numero in enumerate(range(0, 5)):
    numeros.append(int(input(f"Digite um valor para a posicao {posicao}: ")))
print("=-"*40)
print(f"Voce digitou os valores {numeros}")
print(f"O maior valor digitado foi {max(numeros)} nas posicoes ", end='')
for i, n in enumerate(numeros):
    if n == max(numeros):
        print(f"{i}...", end=' ')
print(f"\nO menor valor digitado foi {min(numeros)} nas posicoes ", end='')
for j, m in enumerate(numeros):
    if m == min(numeros):
        print(f"{j}...", end=' ')
print("\n")