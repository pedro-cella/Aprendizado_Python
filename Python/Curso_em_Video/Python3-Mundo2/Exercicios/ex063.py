print("====== DESAFIO 63 ======")
print("""Sobre o programa: Escreva um programa que leia um numero n inteiro qualquer e mostra
na tela os n primeiros elementos de uma Sequencia de Fibonacci.""")
numero = int(input("Quantos termos deseja mostrar:  "))
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2), end='')
contador = 3
while contador <= numero:
    t3 = t1 + t2
    print(" -> {}".format(t3), end='')
    contador += 1
    t1 = t2
    t2 = t3
print(" -> FIM")