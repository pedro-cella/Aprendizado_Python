positivos = 0
soma = 0
for i in range(0, 6):
    numero = float(input())
    if numero > 0:
        positivos += 1
        soma += numero

media = soma/positivos
print(f"{positivos} valores positivos\n{media:.1f}")