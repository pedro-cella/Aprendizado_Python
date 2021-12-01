print("====== DESAFIO 49 ======")
print("""Sobre o programa: Refaca o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher, 
so que agora utilizando um laco for""")
numero = int(input("Escolha um numero para mostra sua tabuada: "))
for m in range(0, 11):
    print("{} x {} = {}".format(numero, m, numero*m))