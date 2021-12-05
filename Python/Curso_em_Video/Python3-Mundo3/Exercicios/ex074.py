from random import randint
print("====== DESAFIO 74 ======")
print("""Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor
que estao na tupla""")
numero1 = randint(0, 100)
numero2 = randint(0, 100)
numero3 = randint(0, 100)
numero4 = randint(0, 100)
numero5 = randint(0, 100)
print(f"Os valores sorteados forma: {numero1} {numero2} {numero3} {numero4} {numero5}")
tupla = (numero1, numero2, numero3, numero4, numero5)
print(f"O maior valor sorteado foi {max(tupla)}")
print(f"O maior valor sorteado foi {min(tupla)}")