from random import randrange
print("====== DESAFIO 58 ======")
print("""Sobre o programa: Melhore o jogo do DESAFIO28 onde o computador vai "pensar" em um numero
entre 0 e 10. So que agora o jogador vai tentar advinhar ate acertar, mostrando no final
quantos palpites foram necessarios para vencer.""")
numero = randrange(11)
soma = 0
escolha = int(input("Sua resposta: "))
while escolha != numero:
    soma += 1
    escolha = int(input("Voce errou! Tente novamente: "))
print("Parabens voce acertou, mas precisou de {} tentativas".format(soma))