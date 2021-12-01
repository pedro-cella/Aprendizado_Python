from math import pow
print("====== DESAFIO 43 ======")
print("""Sobre o programa: Desenvolva uma logica que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu statu, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade morbida""")
peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
imc = peso/pow(altura, 2)
if imc < 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc <= 30:
    print("Sobrepeso")
elif imc > 30 and imc <= 40:
    print("Sobrepeso")
else:
    print("Obesidade morbida")