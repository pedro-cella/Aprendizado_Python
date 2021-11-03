print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {}  de {}".format(rodada, total_de_tentativas))
    
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Voce deve digitar um numero entre 1 e 100!")
        continue


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Voce acertou!")
        break
    else:
        if maior:
            print("Voce errou! O seu chute foi maior do que o numero")
        elif menor:
            print("Voce errou! O seu chute foi menor do que o numero")

print("Fim do jogo")