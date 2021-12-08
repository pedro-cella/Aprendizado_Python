import time
print("====== DESAFIO 98 ======")
print("""Sobre o programa: Faca um programa que tenha uma funcao chamada contador()
que receba tres parametros: inicio, fim, e passo e realize a contagem.
Seu programa tem que realizar tres contagens atraves da funcao criada:
A) De 1 ate 10, de 1 em 1
B) De 10 ate 0, de 2 em 2
C) Uma contagem personalizada""")
def contador(inicio, fim, passo):
    print("-="*30)
    print("Contagem de 1 ate 10 de 1 em 1")
    for i in range(1, 11, 1):
        print(f"{i} ", end='')
    print("FIM!")
    print("-="*30)
    print("Contagem de 10 ate 0 de 2 em 2")
    for i in range(10, -1, -2):
        print(f"{i} ", end='')
    print("FIM!")
    print("-="*30)
    print("Agora e sua vez de personalizar a contagem!")
    inicio = int(input("Inicio: "))
    fim = int(input("Fim:    "))
    passo = int(input("Passo:  "))
    if passo == 0:
        passo += 1
    print("-="*30)
    if passo < 0:
        print(f"Contagem de {inicio} ate {fim} de {-passo} em {-passo}")  
    else:
        print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")
    if inicio > fim and passo < 0:
        for i in range(inicio, fim-1, passo):
            print(f"{i} ", end='')
            time.sleep(1)
    elif inicio > fim:
        for i in range(inicio, fim-1, -passo):
            print(f"{i} ", end='')
    elif passo == 0:
        passo += 1
        for i in range(inicio, fim, passo):
            print(f"{i} ", end='')
    else:
        for i in range(inicio, fim, passo):
            print(f"{i} ", end='')
            time.sleep(1)
    print("FIM!")
contador(1, 1, 1)