print("====== DESAFIO 33 ======")
print("""Sobre o programa: Faca um programa que leia tres numros e mostre
qual e o MAIOR e qual e o MENOR""")
numero1 = int(input("Insira o primeiro numero: "))
numero2 = int(input("Insira o segundo numero: "))
numero3 = int(input("Insira o terceiro numero: "))
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
else:
    maior = numero3
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
else:
    menor = numero3
print("""Maior: {}
Menor: {}""".format(maior, menor))
