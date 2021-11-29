print("====== DESAFIO 35 ======")
print("""Sobre o programa: Desenvolva um programa que leia o comprimento
de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.""")
print("Insira o comprimento de 3 retas")
reta1 = int(input("Insira o valor da primeira reta: "))
reta2 = int(input("Insira o valor da segunda reta: "))
reta3 = int(input("Insira o valor da terceira reta: "))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("E possivel formar um triangulo!")
else:
    print("Nao e possivel formar um triangulo!")
