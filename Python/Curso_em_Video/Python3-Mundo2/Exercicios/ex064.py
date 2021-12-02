print("====== DESAFIO 64 ======")
print("""Sobre o programa: Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. No final, mostre
quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)""")
contador = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input("Insira um numero: "))
    soma += numero
    contador += 1
    if numero == 999:
        soma -= 999
        contador -= 1
print("A soma dos {} numeros inseridos foi de {}".format(contador, soma))
