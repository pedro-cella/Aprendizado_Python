print("====== DESAFIO 32 ======")
print("""Sobre o programa: Faca um programa que leia um ano qualquer e mostre se ele e BISSEXTO""")
ano = int(input("Insira um ano qualquer: "))
if ano%4 == 0:
    print("E ano BISSEXTO")
else:
    print("Nao e ano BISSEXTO")