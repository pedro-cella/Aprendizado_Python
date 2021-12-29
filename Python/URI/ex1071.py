x = int(input())
y = int(input())
soma = 0
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x

menor += 1

while(menor < maior):
    if menor % 2 != 0:
        soma += menor
    menor += 1

print(soma)