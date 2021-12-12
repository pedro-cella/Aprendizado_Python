print("====== DESAFIO 107 ======")
print("""Sobre o programa: Crie um modulo chamado moeda.py que tenha as funcoes incorporadas aumentar(),
diminuir(), dobro() e metade().
Faca tambem um programa que importe esse modulo e use algumas dessas funcoes.""")

def aumentar(valor, quantidade):
    valor += valor*(quantidade/100)
    return valor


def diminuir(valor, quantidade):
    valor -= valor*(quantidade/100)
    return valor


def dobro(valor):
    valor *= 2
    return valor


def metade(valor):
    valor /= 2
    return valor