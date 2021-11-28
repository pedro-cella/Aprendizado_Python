from math import sqrt, floor
import random
num = random.randint(1, 10)
print(num)

num = int(input("Digite um numero: "))
raiz = sqrt(num)
print("A raiz de {} e igual a {:.2f}".format(num, floor(raiz)))