print("====== DESAFIO 75 ======")
print("""Sobre o programa: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posicao foi digitado o primeiro valor 3
C) Quais foram os numeros pares.""")
numero1 = int(input("Insira o primeiro numero: "))
numero2 = int(input("Insira o segundo numero: "))
numero3 = int(input("Insira o terceiro numero: "))
numero4 = int(input("Insira o quarto numero: "))
tupla = (numero1, numero2, numero3, numero4)
print(f"Voce digitou os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if tupla.count(3) == 0:
    print("O valor 3 nao foi digitado em nenhuma posicao")
else:
    print(f"O valor 3 apareceu na {tupla.index(3) + 1}ª posicao")
print("Os valores pares digitados foram: ", end='')
for pos, numero in enumerate(tupla):
    if numero % 2 == 0:
        print(numero, end=' ')
print("\n")