print("====== DESAFIO 10 ======")
print("Sobre o programa: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre\n", end='')
print("quantos Dolares ela pode comprar. Considere US$1.00 = R$3.27")
carteira = float(input("Quantos reais voce tem? "))
print("Com R${:.2f} voce pode comprar US${:.2f}".format(carteira, carteira/3.27))