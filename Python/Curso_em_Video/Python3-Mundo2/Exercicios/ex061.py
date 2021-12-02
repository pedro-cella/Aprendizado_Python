print("====== DESAFIO 61 ======")
print("""Sobre o programa: Refaca o DESAFIO 051 lendo primeiro termo e a razao de uma PA,
mostrando os 10 primeiros termos da progressao usando a estrutura while.""")
a1 = int(input("Primeiro termo: "))
r = int(input("Razao: "))
n = 1
while n != 11:
    formula = a1 + (n-1)*r
    print("a{} = {}".format(n, formula))
    n += 1