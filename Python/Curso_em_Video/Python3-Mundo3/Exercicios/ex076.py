print("====== DESAFIO 76 ======")
print("""Sobre o programa: Crie um programa que tenha uma tupla unica com nomes de produtos e
seus respectivos precos, na sequencia.
No final, mostre uma listagem de precos organizando os dados em forma tabular.""")
listagem = ('Pao', 1, 'Leita', 3.50, 'Frango', 10.90)
print("-"*40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print("-"*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end='')
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-"*40)