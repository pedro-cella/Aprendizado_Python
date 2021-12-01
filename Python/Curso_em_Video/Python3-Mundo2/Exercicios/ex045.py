import random
print("====== DESAFIO 45 ======")
print("""Sobre o programa: Crie um programa que faca o compuador jogar Jokenpo com voce""")
print("Escolha \n1- Pedra\n2- Papel\n3- Tesoura")
sua_mao = int(input("Pedra, papel ou tesoura... "))
mao_computador = random.choice(['pedra', 'papel', 'tesoura'])
if sua_mao == 1:
    print("Voce jogou pedra e o computador {}".format(mao_computador))
    if mao_computador == 'papel':
        print("Voce PERDEU!")
    elif mao_computador == 'tesoura':
        print("Voce GANHOU!")
    else:
        print("Deu EMPATE!")
elif sua_mao == 3:
    print("Voce jogou tesoura e o computador {}".format(mao_computador))
    if mao_computador == 'papel':
        print("Voce GANHOU!")
    elif mao_computador == 'pedra':
        print("Voce PERDEU!")
    else:
        print("Deu EMPATE!")
elif sua_mao == 2:
    print("Voce jogou papel e o computador {}".format(mao_computador))
    if mao_computador == 'tesoura':
        print("Voce PERDEU!")
    elif mao_computador == 'pedra':
        print("Voe GANHOU!")
    else:
        print("Deu EMPATE!")
