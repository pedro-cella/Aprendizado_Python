print("====== DESAFIO 66 ======")
print("""Sobre o programa: Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai 
parar quando o usuario digitar o valor 999, que e a condicao de parada. No final, mostre quantos numeros
foram digitados e qual foi a soma entre eles.""")
numero = contador = 0
soma = 0
while True:
    numero = int(input("Insira um numero(999 para parar): "))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f"Foram digitados {contador} numeros e a soma entre eles e {soma}")

