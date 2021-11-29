print("====== DESAFIO 31 ======")
print("""Sobre o programa: Desenvolva um programa que pergunte a distancia de uma viagem
em Km. Calcule o preco da passagem, cobrando R$0.50 por Km para viagens de ate 200Km e R$0.45
para viagens mais longas.""")
distacia_viagem = float(input("Insira a distancia da viagem: "))
if distacia_viagem <= 200:
    preco_viagem = distacia_viagem*0.50
    print("O preco pela distancia custa R$0.50, o total seria R${}".format(preco_viagem))
else:
    preco_viagem = distacia_viagem*0.45
    print("O preco pela distancia custa R$0.45, o total seria R${}".format(preco_viagem))
