print("====== DESAFIO 42 ======")
print("""Sobre o programa: Refaca o DESAFIO 35 dos triangulos acrescentando o recurso
de mostrar que tipo de triangulo sera formado:
- Equilatero: todos os lados iguais
- Isosceles: dois lados iguais
- Escalenos: todos os lados diferentes""")
print("Insira o comprimento de 3 retas")
reta1 = int(input("Insira o valor da primeira reta: "))
reta2 = int(input("Insira o valor da segunda reta: "))
reta3 = int(input("Insira o valor da terceira reta: "))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("E possivel formar um triangulo!")
    if reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
        print("E um triangulo EQUILATERO")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("E um triangulo ISOSCELES")
    else:
        print("E um triangulo ESCALENO")
else:
    print("Nao e possivel formar um triangulo!")
