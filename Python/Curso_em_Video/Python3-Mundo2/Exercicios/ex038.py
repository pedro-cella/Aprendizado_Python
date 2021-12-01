print("====== DESAFIO 38 ======")
print("""Sobre o programa: Escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor e maior;
- O segundo valor e maior;
- Nao existe valor maior, os dois sao iguais""")
numero1 = int(input("Insira o primeiro numero: "))
numero2 = int(input("Insira o segundo numero: "))
if numero1 > numero2:
    print("O primeiro valor e maior")
elif numero1 < numero2:
    print("O segundo valor e maior")
else:
    print("Nao existe valor maior, os dois sao iguais")