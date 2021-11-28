from math import floor, ceil
print("====== DESAFIO 16 ======")
print("Sobre o programa: Crie um programa que leia um numero Real qualquer pelo teclado", end='')
print("e mostre na tela a sua porcao inteira.", end='')
print("Ex: Digite um numero: 6.127\nO numero 6.127 tem a parte Inteira 6")
numero = float(input("Digite um numero: "))
inteiro = int(numero)
print("O numero {} tem a parte inteira {}.".format(numero, inteiro))
# Ou
# print("O numero {} tem a parte inteira {}.".format(numero, floor(numero)))