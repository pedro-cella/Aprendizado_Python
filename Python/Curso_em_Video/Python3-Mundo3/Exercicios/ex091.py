from random import randint
import time
print("====== DESAFIO 91 ======")
print("""Sobre o programa: Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatorios. Guarde esses resultados em um dicionario. No final, coloque esse
dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.""")
jogo = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
jogo['jogador1'] = randint(1, 6)
jogo['jogador2'] = randint(1, 6)
jogo['jogador3'] = randint(1, 6)
jogo['jogador4'] = randint(1, 6)
print("Valores sortedos: ")
for k, v in jogo.items():
    time.sleep(1)
    print(f"    O {k} tirou {v}")
print("Ranking dos jogadores: ")
ranking = dict(sorted(jogo.items(), key = lambda x: x[1]))
contador = 1
for k, v in ranking.items():
    time.sleep(1)
    print(f"    O {contador}º lugar: {k} com {v}")
    contador += 1