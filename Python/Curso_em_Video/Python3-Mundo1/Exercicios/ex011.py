print("====== DESAFIO 11 ======")
print("Sobre o programa: Faca um programa que leia a largura e a altura\n", end='')
print("de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la,\n", end='')
print("sabendo que cada litro de tinta pinta uma area de 2m^2\n", end='')
largura = float(input("Insira a largura: "))
altura = float(input("Insira a altura: "))
print("A area da parede eh {}m^2, sendo necessario {} litros de tinta".format(largura*altura, (largura*altura/2)))