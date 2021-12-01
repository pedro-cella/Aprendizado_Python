import time
print("====== DESAFIO 46 ======")
print("""Sobre o programa: Faca um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles.""")
for fogos in range(10, -1, -1):
    print(fogos)
    time.sleep(1)
print("Boom")