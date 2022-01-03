lista = []
n1, n2, n3 = map(float, input().split())
lista.append(n1)
lista.append(n2)
lista.append(n3)

lista.sort(reverse=True)

c = lista.pop()
b = lista.pop()
a = lista.pop()

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == ((b**2) + (c**2)):
        print("TRIANGULO RETANGULO")
    if a**2 > ((b**2) + (c**2)):
        print("TRIANGULO OBTUSANGULO")
    if a**2 < ((b**2) + (c**2)):
        print("TRIANGULO ACUTANGULO")
    if a == b and a == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")