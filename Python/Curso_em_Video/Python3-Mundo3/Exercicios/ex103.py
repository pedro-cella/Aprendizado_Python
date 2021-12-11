print("====== DESAFIO 103 ======")
print("""Sobre o programa: Faca um programa que tenha uma funcao chamada ficha(), que recebe dois parametros
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado
corretamente.""")
def ficha(jog="<desconhecido>", gol=0):
    return print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")


print("-"*15)
n = str(input("Nome do Jogador: "))
g = str(input("Numero de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)