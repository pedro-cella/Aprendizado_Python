print("====== DESAFIO 12 ======")
print("Sobre o programa: Faca um algoritmo que leia o preco de um produto", end='')
print("e mostre seu novo precom com 5% de desconto")
preco = float(input("Insira o preco do produto: "))
desconto = preco - (preco * 0.05)
print("O valor do produto e {}, com 5% de esconto fica {:.2f}".format(preco, desconto))