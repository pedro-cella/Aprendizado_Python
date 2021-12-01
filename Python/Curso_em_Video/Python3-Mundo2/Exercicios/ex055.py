print("====== DESAFIO 55 ======")
print("""Sobre o programa: Faca um programa que leia o peso de cinco pessoas.
No final mostre qual foi o maior e o menor peso lidos""")
maior = 0
menor = 10000
for i in range(1, 6):
    peso = float(input("Pessoa {} - Insira seu peso: ".format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print("Maior Peso: {}\nMenor Peso: {}".format(maior, menor))