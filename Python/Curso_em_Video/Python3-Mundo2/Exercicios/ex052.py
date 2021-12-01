print("====== DESAFIO 52 ======")
print("""Sobre o programa: Faca um programa que leia um numero inteiro e diga se ele e ou nao
um numero primo""")
numero = int(input("Insira um numero: "))
soma = 0
for i in range(1, 11):
    if numero%i == 0:
        soma += 1
if soma <= 2:
    print("E um numero primo")
else:
    print("Nao e um numero primo")