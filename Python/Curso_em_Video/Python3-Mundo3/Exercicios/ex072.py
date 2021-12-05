print("====== DESAFIO 72 ======")
print("""Sobre o programa: Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extendo, de zero ate vinte.
Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso""")
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'deszoito', 'dezenove', 'vinte')
escolha = int(input("Digite um numero entre 0 e 20: "))
while escolha > 20 or escolha < 0:
    print("Tente novamente.", end=' ')
    escolha = int(input("Digite um numero entre 0 e 20: "))
print(f"Voce digitou o numero {numeros[escolha]}")