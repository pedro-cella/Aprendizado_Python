from math import hypot
print("====== DESAFIO 17 ======")
print("Sobre o programa: Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente", end='')
print("de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa")
cateto_oposto = int(input("Insira o valor do cateto oposto: "))
cateto_adjacente = int(input("Insira o valor do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print("O valor da hipotenusa e: {:.0f}".format(hipotenusa))