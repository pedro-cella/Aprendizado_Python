print("====== DESAFIO 67 ======")
print("""Sobre o programa: Faca um programa que mostre a tabuada de varios numeros, um de cada vez,
para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo.""")
n = 0
while True:
    n = int(input("Insira um numero(numero negativo para parar): "))
    if n < 0:
        break
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")