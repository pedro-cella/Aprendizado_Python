print("====== DESAFIO 34 ======")
print("""Sobre o programa: Escreva um programa que pergunte o salario de um funcionario
e calcule o valor do seu aumento.
Para salarios superiores a R$1250.00 calcule um aumento de 10%
Para is inferiores ou iguais, o aumento e de 15%""")
salario = float(input("Insira seu salario: "))
if salario > 1250.00:
    novo_salario = salario + (salario*(10/100))
    print("Seu salario com aumento de 10% e de: {:.2f}".format(novo_salario))
else:
    novo_salario = salario + (salario*(15/100))
    print("Seu salario com aumento de 15% e de: {:.2f}".format(novo_salario))
