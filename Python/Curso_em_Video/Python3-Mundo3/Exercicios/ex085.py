print("====== DESAFIO 85 ======")
print("""Sobre o programa: Crie um programa onde o usuario possa digitar sete valores numericos
e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. No final,
mostre os valores pares e impares em ordem crescente.""")
lista = list()
pares = list()
impares = list()
for i in range(0, 7):
    numero = int(input(f"Digite o {i}o valor: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
lista.append(pares[:])
lista.append(impares[:])
for count, n in enumerate(lista):
    if n[count] % 2 == 0:
        n.sort()
        print(f"Os valores pares digitados foram: {n}")
    else:
        n.sort()
        print(f"Os valores impares digitados foram: {n}")