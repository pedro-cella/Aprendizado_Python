import moeda

p = float(input("Digite o preco: R$"))
print(f"A metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p), True)}")
print(f"O dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p), True)}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10), True)}")
print(f"Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}")