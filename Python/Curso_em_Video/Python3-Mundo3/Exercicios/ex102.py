print("====== DESAFIO 102 ======")
print("""Sobre o programa: Crie um programa que tenha uma funcao fatorial() que receba dois parametros: 
o primeiro que indique o numero a calcular e o outro shamado show, que sera um valor logico(opicional) indicando
se sea mostrado ou nao na tela o processo de calculo do fatorial.""")
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opicional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um numero n.
    """
    if show == False:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            if c == 1:
                print(f"{c} = ", end='')
            else:
                print(f"{c} x ", end='')
        return f

print("-"*15)
print(fatorial(5, show=False))