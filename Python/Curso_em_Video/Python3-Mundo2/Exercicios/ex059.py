print("====== DESAFIO 59 ======")
print("""Sobre o programa: Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Seu programa devera realizar a operacao solicitada em cada caso\n""")

numero1 = int(input("Insira o valor do primeiro numero: "))
numero2 = int(input("Insira o valor do segundo numero: "))
escolha = 0
maior = 0
while escolha != 5:
    print("""[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa""")
    escolha = int(input("Sua escolha: "))
    if escolha == 1:
        soma = numero1 + numero2
        print("A soma dos numeros {} e {} e {}\n".format(numero1, numero2, soma))
    elif escolha == 2:
        multiplicacao = numero1 * numero2
        print("A multiplicacao dos numeros {} e {} e {}\n".format(numero1, numero2, multiplicacao))
    elif escolha == 3:
        if numero1 > numero2:
            maior = numero1
            print("O maior numero e o {}\n".format(maior))
        elif numero1 < numero2:
            maior = numero2
            print("O maior numero e o {}\n".format(maior))
        else:
            print("Os numeros sao iguais\n")
    elif escolha == 4:
        print("Inserir novos valores")
        numero1 = int(input("Insira o novo valor do primeiro numero: "))
        numero2 = int(input("Insira o novo valor do segundo numero: "))
print("FIM")