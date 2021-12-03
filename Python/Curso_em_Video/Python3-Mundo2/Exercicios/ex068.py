import random
print("====== DESAFIO 68 ======")
print("""Sobre o programa: Faca um programa que jogue par ou impar
com o computador. O jogo so sera interrompido quando o jogador PERDER,
mostrando o total de vitorias consecutivas que ele conquistou no final do jogo""")
contador_vitoria = 0
while True:
    escolha = input("Par ou Impar: ")
    computador = random.choice(["par", "impar"])
    if escolha == computador:
        print("Voce GANHOU")
        contador_vitoria += 1
    else:
        print("Voce PERDEU!")
        break
print(f"Voce ganhou {contador_vitoria} vez(es)")