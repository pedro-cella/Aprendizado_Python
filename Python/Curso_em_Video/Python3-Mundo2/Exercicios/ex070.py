print("====== DESAFIO 70 ======")
print("""Sobre o programa: Crie um programa que leia o nome e o preco de varios produtos. O programa
devera perguntar se o usuario vai continuar. No final, mostre:
A) Qual e o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual e o nome do produto mais barato""")
total = 0
quantidade = 0
barato = 1000
while True:
    nome = input("Nome do produto: ")
    preco = float(input("Insira o preco do produto: R$"))
    total += preco
    if preco > 1000:
        quantidade += 1
    elif preco < barato:
        mais_barato = nome
    decisao = input("Deseja continuar [S/N]: ").upper()
    if decisao == 'N':
        break
print(f"""Total Gasto: {total}
Total de produtos com preco maior que R$1000.00: {quantidade}
Nome do produto mais barato: {mais_barato}""")
    