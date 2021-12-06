print("====== DESAFIO 83 ======")
print("""Sobre o programa: Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
Seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.""")
lista = []
expressao = input("Digite a expressao: ")
lista = list(expressao)
primeiro_parenteses = lista.count("(")
segundo_parenteses = lista.count(")")
if primeiro_parenteses == segundo_parenteses:
    print("Essa expressao e valida!")
else:
    print("Sua expressao esta errada!")