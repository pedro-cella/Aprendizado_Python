print("====== DESAFIO 109 ======")
print("""Sobre o programa: Modifique as funcoes que foram criadas no desfio 107 para que elas aceitem um parametro
a mais, informando se o calor retornado por elas vai ser ou nao formatado pela funcao moeda(), desenvolvido no
desafio 108""")

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


def moeda(valor, format=False):
    if format == True:
        return f"R${valor:.2f}"
    else:
        return f"{valor}"