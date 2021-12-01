print("====== DESAFIO 37 ======")
print("""Sobre o programa: Escreva um programa que leia um numero inteiro qualquer e peca
para o usuario escolher qual sera a base de conversao:
- 1 para binario
- 2 para octal
- 3 para hexadecimal""")
numero = int(input("Insira um numero: "))
print("Para qual base deseja converter o numero: \n1- Binario\n2- Octal\n3- Hexadecimal\n")
escolha = int(input("Escolha: "))
if escolha == 1:
    binario = bin(numero)
    print("Binario = {}".format(binario))
elif escolha == 2:
    octal = oct(numero)
    print("Octal = {}".format(octal))
else:
    hexadecimal = hex(numero)
    print("Hexadecimal = {}".format(hexadecimal))