print("====== DESAFIO 86 ======")
print("""Sobre o programa: Crie um programa que crie uma matriz de dimensao 3x3 e
prencha com valores lidos pelo teclado""")
matriz = list()
linha = 3
coluna = 3

for i in range(linha):
    n = []
    for j in range(coluna):
        n.append(int(input(f"Digite um valor para {[i, j]}: ")))
    matriz.append(n)
print("-="*30)
for i in range(linha):
    for j in range(coluna):
        print(f"[ {matriz[i][j]} ]", end=" ")
    print()