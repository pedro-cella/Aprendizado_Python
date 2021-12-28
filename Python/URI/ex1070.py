x = int(input())
impares = 0
while impares != 6:
    if x % 2 != 0:
        impares += 1
        print(x)
    x += 1
