contador = 0
for i in range(0, 6):
    numero = float(input())
    if numero > 0:
        contador += 1
print(f"{contador} valores positivos")