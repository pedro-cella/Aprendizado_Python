print("====== DESAFIO 87 ======")
print("""Sobre o programa: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna.
C) O maior valo da segunda linha""")
matriz = []
linha = 3
coluna = 3
soma = 0
terceira_coluna = 0
maior = 0
for i in range(linha):
    n = []
    for j in range(coluna):
        numero = int(input(f"Digite um valor {[i, j]}: "))
        n.append(numero)
        if numero % 2 == 0:
            soma += numero
        if j == 2:
            terceira_coluna += numero
        if i == 1 and numero > maior:
            maior = numero   
    matriz.append(n)
print("-="*30)
for i in range(linha):
    for j in range(coluna):
        print(f"[ {matriz[i][j]} ]", end=' ')
    print()
print(f"A soma dos valores pares e {soma}")
print(f"A soma dos valores da terceira coluna e {terceira_coluna}")
print(f"O maior valor da segunda linha e {maior}")