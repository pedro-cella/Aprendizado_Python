import moeda

p = float(input("Digite o preco: R$"))
print(f"A metade de {p} e {moeda.metade(p)}")
print(f"O dobro de {p} e {moeda.dobro(p)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13)}")