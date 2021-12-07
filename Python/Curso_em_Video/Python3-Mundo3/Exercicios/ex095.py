print("====== DESAFIO 95 ======")
print("""Sobre o programa: Aprimore o DESAFIO 93 para que ele funcione com varios jogadores, incluindo
um sistema de visualizacao de detalhes do aproveitamento de cada jogador.""")
gols = []
aproveitamento = {}
escolha = 'S'
jogadores = []
contador = 0
while escolha != 'N':
    aproveitamento.clear()
    aproveitamento['cod'] = contador
    contador += 1
    nome = input("Nome do Jogador: ")
    aproveitamento['nome'] = nome
    qtd_partidas = int(input(f"Quantas partidas {nome} jogou? "))
    for i in range(qtd_partidas):
        gols.append(int(input(f"    Quantos gols na partida {i}? ")))
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = sum(gols)
    gols.clear()
    jogadores.append(aproveitamento.copy())
    escolha = input("Quer continuar? [S/N] ").upper()
    print("-"*30)
print("-="*30)
print("cod    nome    gols    total")
print("-"*30)
for k, v in enumerate(jogadores):
    print(f"{v['cod']}    {v['nome']}    {v['gols']}    {v['total']}")
while True:
    numero = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if numero == 999:
        break
    if numero >= len(jogadores):
        print(f"ERRO! Nao existe jogador com codigo {numero}")
    else:
        print(f"-- LEVANTAMENTO DE DADOS DO JOGADOR {jogadores[numero]['nome']}: ")
        for k, v in enumerate(jogadores[numero]['gols']):
            print(f"    No jogo {k} fez {v} gols.")        