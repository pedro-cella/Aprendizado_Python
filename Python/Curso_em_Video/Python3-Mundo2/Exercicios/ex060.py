print("====== DESAFIO 60 ======")
print("""Sobre o programa: Faca um programa que leia um numero qualquer e mostre o seu fatorial.""")
numero = int(input("Insira um numero: "))
contador = 1
fatorial = 1
while contador <= numero:
    fatorial *= contador
    contador += 1
print(fatorial)