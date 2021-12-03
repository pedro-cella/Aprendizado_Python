print("====== DESAFIO 69 ======")
print("""Sobre o programa: Crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos""")
pessoas_maiores = 0
homens = 0
mulheres = 0
while True:
    idade = int(input("Insira sua idade: "))
    sexo = input("Insira seu sexo(M ou F): ").upper()
    if idade >= 18:
        pessoas_maiores += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    decisao = input("Deseja continuar(S/N): ").upper()
    if decisao == 'N':
        break
print(f"Maiores de 18: {pessoas_maiores}\nNumero de homens: {homens}\nMulheres com menos de 20 anos: {mulheres}")
