print("====== DESAFIO 14 ======")
print("Sobre o programa: Escreva um programa que pergunta a quantidade de Km percorridos", end='')
print("por um carro alugado e a quantidade de dias pelos quais ele foi alugado.", end='')
print("Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.")
dias = int(input("Quantos dias alugados? "))
quilometros = int(input("Quantos Km rodados? "))
total = (dias*60) + (0.15*quilometros)
print("O total a pagar e de R${:.2f}".format(total))