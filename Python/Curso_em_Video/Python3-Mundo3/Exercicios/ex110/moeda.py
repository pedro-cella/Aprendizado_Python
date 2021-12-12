print("====== DESAFIO 109 ======")
print("""Sobre o programa: Adicione ao modulo moeda.py criado nos desafios anteriores, uma funcao chamada resumo(),
que mostre na tela algumas informacoes geradas pelas funcoes que ja temos
no modulo criado ate aqui.""")

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

def resumo(valor, aumento, reducao):
    print("-"*40)
    msg = "RESUMO DO VALOR"
    resultado = msg.center(40)
    print(resultado)
    print("-"*40)
    print("{:<10}{:>23}".format("Preco analisado: ", moeda(valor, True)))
    print("{:<10}{:>24}".format("Dobro do preco: ", moeda(dobro(valor), True)))
    print("{:<10}{:>23}".format("Metade do preco: ", moeda(metade(valor), True)))
    print("{}% {:<10}{:>24}".format(aumento, "de aumento: ", moeda(aumentar(valor, aumento), True)))
    print("{}% {:<10}{:>24}".format(reducao, "de reducao: ", moeda(diminuir(valor, reducao), True)))
    print("-"*40)