print("====== DESAFIO 48 ======")
print("""Sobre o programa: Faca um programa que calcule a soma entre todos os numeros impares
que sao multiplos de tres e que se encontram no intervalo de 1 ate 500.""")
s = 0
for n in range(1, 501):
    if n%2 != 0 and n%3 == 0:
        s += n
print(s)