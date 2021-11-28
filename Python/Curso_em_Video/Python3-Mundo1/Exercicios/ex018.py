from math import sin, cos, tan
print("====== DESAFIO 18 ======")
print("Sobre o programa: Faca um programa que leia um angulo qualquer e mostre", end='')
print("na tela o valor do seno, cosseno e tangente desse angulo")
angulo = int(input("Insira um angulo: "))
print("O angulo {}, possui o valor {:.0f} como seno".format(angulo, sin(angulo)), end='')
print(" o valor {:.0f} como cosseno e o valor {:.0f} como tangente".format(cos(angulo), tan(angulo)))