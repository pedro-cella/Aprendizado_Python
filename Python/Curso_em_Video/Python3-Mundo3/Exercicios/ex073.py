print("====== DESAFIO 73 ======")
print("""Sobre o programa: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocacao. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os ultims 4 colocados da tabela.
C) Uma lista com os times em ordem alfabetica.
D) Em que posicao na tabela esta o time da Chapecoense""")
times = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino',
'Fluminense', 'America-MG', 'Ceara-SC', 'Internacional', 'Atletic-GO', 'Santos', 'Atletico-PR', 'Sao Paulo',
'Juventude', 'Cuiaba', 'Bahia', 'Gremio', 'Sport Recife', 'Chapecoense')
print("-="*50)
print(f"Lista de times do Brasileirao: {times}")
print("-="*50)
print(f"Os 5 primeiros sao: {times[:6]}")
print("-="*50)
print(f"Os 4 ultimos sao: {times[-4:]}")
print("-="*50)
print(f"Times em ordem alfabetica: {sorted(times)}")
for c, i in enumerate(times):
    if i == 'Chapecoense':
        print(f"O Chapecoense esta na {c}º posicao")
print("-="*50)