print("====== DESAFIO 65 =====")
print("""Sobre o programa: Crie um programa que leia varios numeros inteiros pelo teclado. No final
da exeucao, mostre a media entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar se o usuario quer ou nao continuar a digitar valores.""")
maior = 0
menor = 10000
soma = 0
escolha = 's'.upper()
contador = 0
while escolha != 'N':
    numero = int(input("Insira um numero: "))
    contador += 1
    soma += numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    escolha = input("Quer continuar?(S ou N): ").upper()
print("A media entre os numeros foi de {}".format(soma/contador))
print("MAIOR NUMERO: {}\nMENOR NUMERO: {}".format(maior, menor))