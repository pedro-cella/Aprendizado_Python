print("====== DESAFIO 62 ======")
print("""Sobre o programa: Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos""")
a1 = int(input("Primeiro termo: "))
r = int(input("Razao: "))
n = 1
escolha = int(input("Quantos termos deseja visualizar? "))
c = escolha
while escolha != 0:
    formula = a1 + (n-1)*r
    print("a{} = {}".format(n, formula))
    n += 1
    c -= 1
    if c == 1:
        escolha = int(input("Quantos termos a mais deseja visualizar? "))
        c = escolha

