print("====== DESAFIO 50 ======")
print("""Sobre o programa: Desenvolva um programa que leia seis numeros inteiros e mostre
apenas aqueles que forem pares. Se o valor digitado for impar, desconsidere-o""")
soma = 0
for i in range(1, 7):
    numero = int(input("Insira um numero: "))
    if numero%2 == 0:
          soma += numero
print(soma)