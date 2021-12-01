print("====== DESAFIO 51 ======")
print("""Sobre o programa: Desenvolva um programa que leia o primeiro temo e a razao de uma PA.
No final, mostre os 10 primeiros temos dessa progressao""")
a1 = int(input("Primeiro termo: "))
r = int(input("Razao: "))
for n in range(1, 11):
    formula = a1 + (n-1)*r
    print("a{} = {}".format(n, formula))