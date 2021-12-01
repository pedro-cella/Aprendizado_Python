print("====== DESAFIO 54 ======")
print("""Sobre o programa: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores""")
maiores = 0
menores = 0
for i in range(1, 8):
    ano_nascimento = int(input("Pessoa {} - Insira seu ano de nascimento: ".format(i)))
    if 2021 - ano_nascimento >= 18:
        maiores += 1
    else:
        menores += 1
print("{} ja atingiram a maioridade e {} ainda sao menores de idade".format(maiores, menores))