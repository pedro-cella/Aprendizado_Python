print("====== DESAFIO 108 ======")
print("""Sobre o programa: Adapte o codigo do desafio 107, criando uma funcao adicional chamada moeda() que consiga
mostrar os valores como um valor monetario formatado.""")

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


def moeda(valor):
    return f"R${valor:.2f}"