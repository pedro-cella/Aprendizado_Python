# contador = 1
# while True:
#     print(contador, '-> ', end='')
#     contador += 1
# print('Acabou')
n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')