print("====== DESAFIO 29 ======")
print("""Sobre o programa: Escreva um programa que leia a velocidade
de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite""")
velocidade = int(input("Insira a velocidade do carro: "))
if velocidade > 80:
    print("Voce foi multado!")
    velocidade_acima = velocidade - 80
    multa = float(7.0*velocidade_acima)
    print("Sua multa e de: R${:.2f}".format(multa))