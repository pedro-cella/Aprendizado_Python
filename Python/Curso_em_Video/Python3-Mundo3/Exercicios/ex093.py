print("====== DESAFIO 93 ======")
print("""Sobre o programa: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso sera guardado em um dicionario, incluindo
o total de gols feitos durante o campeonato.""")
gols = []
aproveitamento = {}
nome = input("Nome do Jogador: ")
aproveitamento['nome'] = nome
qtd_partidas = int(input(f"Quantas partidas {nome} jogou? "))
for i in range(qtd_partidas):
    partida = int(input(f"Quantos gols na partida {i}? "))
    gols.append(partida)
    aproveitamento['gols'] = gols
total = sum(gols)
aproveitamento['total'] = total
print("-="*30)
print(aproveitamento)
print("-="*30)
for k, v in aproveitamento.items():
    print(f"O campo {k} tem o valor {v}.")
print("-="*30)
print(f"O jogador {aproveitamento['nome']} jogou {len(aproveitamento['gols'])} partidas.")
for i in range(len(aproveitamento['gols'])):
    print(f"    => Na partida {i}, fez {aproveitamento['gols'][i]}")
print(f"Foi um total de {aproveitamento['total']} gols.")