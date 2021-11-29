from random import randrange
print("====== DESAFIO 28 ======")
print("""Sobre o programa: Escreva um programa que faca o computador "pensar"
entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador
O programa devera escrever na tela se o usuario venceu ou perdeu""")
print("Descubra qual numero entre 0 e 5 o computador esta pensando\n")
numero = randrange(6)
escolha = int(input("Sua resposta: "))
if escolha == numero:
    print("Parabens voce VENCEU!")
else:
    print("Voce PERDEU!")