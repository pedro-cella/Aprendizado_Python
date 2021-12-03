print("====== DESAFIO 71 ======")
print("""Sobre o programa: Crie um programa que simule o funcionamento de um caixa eletronico. No
inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas
cedulas de cada valor serao entregues.
OBS: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.""")
valor = int(input("Informe o valor que deseja sacar: R$"))
cedula = 50
total = valor
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f"Total de {total_cedula} cedulas de R${cedula}")
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula  = 0
        if total == 0:
            break